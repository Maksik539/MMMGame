"""
Main level editor for Mage Quest
"""
import pygame
import config
from src.editor.room_editor import RoomEditor
from src.editor.texture_loader import TextureLoader
from src.editor.texture_panel import TexturePanel
from src.editor.animation_loader import AnimationLoader
from src.editor.animation_panel import AnimationPanel
from src.editor.properties_panel import PropertiesPanel
from src.editor.tabs_panel import TabsPanel
from src.editor.minimap_panel import MinimapPanel
from src.editor.connections_panel import ConnectionsPanel
from src.editor.passages_panel import PassagesPanel
from src.editor.undo_redo import HistoryManager
from src.editor.level_utils import LevelUtils


class LevelEditor:
    """Main level editor application"""
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("Mage Quest - Level Editor")
        self.clock = pygame.time.Clock()
        self.running = False
        
        # Initialize components
        self.texture_loader = TextureLoader()
        self.animation_loader = AnimationLoader()
        self.room_editor = RoomEditor(50, 40)
        self.history = HistoryManager()
        
        # UI Panels
        self.texture_panel = TexturePanel(10, 10, 200, 400, self.texture_loader)
        self.animation_panel = AnimationPanel(10, 420, 200, 290, self.animation_loader)
        self.properties_panel = PropertiesPanel(220, 10, 300, 200)
        self.tabs_panel = TabsPanel(220, 220, 300, 200)
        self.minimap_panel = MinimapPanel(
            config.SCREEN_WIDTH - 260,
            10,
            250,
            250
        )
        self.connections_panel = ConnectionsPanel(
            config.SCREEN_WIDTH - 260,
            270,
            250,
            200
        )
        self.passages_panel = PassagesPanel(
            config.SCREEN_WIDTH - 260,
            480,
            250,
            230
        )
        
        self.panels = [
            self.texture_panel,
            self.animation_panel,
            self.properties_panel,
            self.tabs_panel,
            self.minimap_panel,
            self.connections_panel,
            self.passages_panel
        ]
        
        # Editor area
        self.editor_rect = pygame.Rect(230, 430, 800, 280)
        
        # Fonts
        self.font = pygame.font.Font(None, 24)
        
    def run(self):
        """Main editor loop"""
        self.running = True
        
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(config.FPS)
            
    def handle_events(self):
        """Handle input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_s and (event.mod & pygame.KMOD_CTRL):
                    self.save_level()
                elif event.key == pygame.K_o and (event.mod & pygame.KMOD_CTRL):
                    self.load_level()
                elif event.key == pygame.K_z and (event.mod & pygame.KMOD_CTRL):
                    self.undo()
                elif event.key == pygame.K_y and (event.mod & pygame.KMOD_CTRL):
                    self.redo()
                    
            # Handle panel events
            handled = False
            for panel in self.panels:
                if panel.handle_event(event):
                    handled = True
                    break
                    
            # Update selected tile from texture panel
            if not handled:
                selected = self.texture_panel.get_selected_texture()
                if selected:
                    self.room_editor.selected_tile = selected
                    
            # Handle room editor events
            if not handled:
                self.room_editor.handle_event(event, self.editor_rect)
                
    def update(self):
        """Update editor state"""
        for panel in self.panels:
            panel.update()
            
    def draw(self):
        """Draw editor"""
        self.screen.fill(config.BLACK)
        
        # Draw room editor
        pygame.draw.rect(self.screen, config.DARK_GRAY, self.editor_rect)
        pygame.draw.rect(self.screen, config.WHITE, self.editor_rect, 2)
        self.room_editor.draw(self.screen, self.editor_rect, self.texture_loader)
        
        # Draw panels
        for panel in self.panels:
            panel.draw(self.screen)
            
        # Draw toolbar
        self.draw_toolbar()
        
        pygame.display.flip()
        
    def draw_toolbar(self):
        """Draw the toolbar"""
        toolbar_rect = pygame.Rect(0, 0, config.SCREEN_WIDTH, 30)
        pygame.draw.rect(self.screen, config.GRAY, toolbar_rect)
        pygame.draw.rect(self.screen, config.WHITE, toolbar_rect, 1)
        
        # Instructions
        text = self.font.render(
            "Ctrl+S: Save | Ctrl+O: Load | Ctrl+Z: Undo | Ctrl+Y: Redo | ESC: Exit",
            True, config.WHITE
        )
        self.screen.blit(text, (10, 5))
        
    def save_level(self):
        """Save the current level"""
        level_data = self.room_editor.get_room_data()
        LevelUtils.save_level(level_data, "level_01.json")
        print("Level saved!")
        
    def load_level(self):
        """Load a level"""
        level_data = LevelUtils.load_level("level_01.json")
        if level_data:
            self.room_editor.load_room_data(level_data)
            self.minimap_panel.set_level(level_data)
            print("Level loaded!")
        else:
            print("No level found!")
            
    def undo(self):
        """Undo last action"""
        action = self.history.undo()
        if action:
            # Apply undo action
            print("Undo")
            
    def redo(self):
        """Redo last undone action"""
        action = self.history.redo()
        if action:
            # Apply redo action
            print("Redo")

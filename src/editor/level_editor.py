"""
Level Editor Main
"""
import pygame
from config import *
from src.editor.texture_loader import texture_loader
from src.editor.texture_panel import TexturePanel
from src.editor.animation_panel import AnimationPanel
from src.editor.animation_loader import animation_loader
from src.editor.tabs_panel import TabsPanel
from src.editor.room_editor import RoomEditor
from src.editor.connections_panel import ConnectionsPanel
from src.editor.minimap_panel import MinimapPanel
from src.editor.properties_panel import PropertiesPanel
from src.editor.level_utils import LevelUtils
from src.editor.undo_redo import HistoryManager


class LevelEditor:
    """Main level editor class"""
    
    def __init__(self):
        """Initialize level editor"""
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("MMMGame - Level Editor")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Editor state
        self.current_level = LevelUtils.create_new_level()
        self.history = HistoryManager()
        
        # Room editor
        self.room_editor = RoomEditor()
        
        # UI Panels
        panel_width = 200
        self.texture_panel = TexturePanel(
            SCREEN_WIDTH - panel_width,
            0,
            panel_width,
            250
        )
        
        self.animation_panel = AnimationPanel(
            SCREEN_WIDTH - panel_width,
            250,
            panel_width,
            200
        )
        
        self.properties_panel = PropertiesPanel(
            SCREEN_WIDTH - panel_width,
            450,
            panel_width,
            150
        )
        
        self.minimap_panel = MinimapPanel(
            SCREEN_WIDTH - panel_width,
            600,
            panel_width,
            120
        )
        
        self.tabs_panel = TabsPanel(0, 0, 400, 30)
        
        self.connections_panel = ConnectionsPanel(
            0,
            SCREEN_HEIGHT - 150,
            300,
            150
        )
        
        # Editor view
        self.view_rect = pygame.Rect(0, 30, SCREEN_WIDTH - panel_width, SCREEN_HEIGHT - 30)
        
        # Initialize
        texture_loader.scan_assets_directory()
    
    def handle_events(self):
        """Handle editor events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    self._save_level()
                elif event.key == pygame.K_o and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    self._load_level()
                elif event.key == pygame.K_z and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    self._undo()
                elif event.key == pygame.K_y and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    self._redo()
                elif event.key == pygame.K_g:
                    self.room_editor.show_grid = not self.room_editor.show_grid
            
            # Handle panel events
            self.texture_panel.handle_event(event)
            self.animation_panel.handle_event(event)
            self.properties_panel.handle_event(event)
            self.minimap_panel.handle_event(event)
            self.tabs_panel.handle_event(event)
            self.connections_panel.handle_event(event)
            
            # Handle room editor events (only if in view area)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.view_rect.collidepoint(event.pos):
                    # Adjust event position to room editor coordinates
                    adjusted_event = pygame.event.Event(
                        event.type,
                        {'pos': (event.pos[0] - self.view_rect.x, 
                                event.pos[1] - self.view_rect.y),
                         'button': event.button}
                    )
                    self.room_editor.handle_event(adjusted_event)
    
    def update(self):
        """Update editor state"""
        # Update selected texture from panel
        selected_texture = self.texture_panel.get_selected_texture()
        if selected_texture:
            self.room_editor.set_current_texture(selected_texture)
        
        # Update camera with arrow keys
        keys = pygame.key.get_pressed()
        camera_speed = 5
        
        if keys[pygame.K_LEFT]:
            self.room_editor.camera_x -= camera_speed
        if keys[pygame.K_RIGHT]:
            self.room_editor.camera_x += camera_speed
        if keys[pygame.K_UP]:
            self.room_editor.camera_y -= camera_speed
        if keys[pygame.K_DOWN]:
            self.room_editor.camera_y += camera_speed
    
    def draw(self):
        """Draw editor"""
        self.screen.fill((30, 30, 30))
        
        # Draw tabs
        self.tabs_panel.draw(self.screen)
        
        # Draw room editor in view area
        view_surface = pygame.Surface((self.view_rect.width, self.view_rect.height))
        self.room_editor.draw(view_surface, self.view_rect)
        self.screen.blit(view_surface, (self.view_rect.x, self.view_rect.y))
        
        # Draw panels
        self.texture_panel.draw(self.screen)
        self.animation_panel.draw(self.screen)
        self.properties_panel.draw(self.screen)
        self.minimap_panel.draw(self.screen, self.current_level)
        self.connections_panel.draw(self.screen)
        
        # Draw status bar
        self._draw_status_bar()
        
        pygame.display.flip()
    
    def _draw_status_bar(self):
        """Draw status bar"""
        font = pygame.font.Font(None, 20)
        
        # Tool info
        tool_text = f"Tool: {self.room_editor.current_tool}"
        text = font.render(tool_text, True, WHITE)
        self.screen.blit(text, (10, SCREEN_HEIGHT - 25))
        
        # Grid toggle info
        grid_text = f"Grid: {'ON' if self.room_editor.show_grid else 'OFF'} (G)"
        text = font.render(grid_text, True, WHITE)
        self.screen.blit(text, (150, SCREEN_HEIGHT - 25))
    
    def _save_level(self):
        """Save current level"""
        # Update level data
        self.current_level['rooms'] = [self.room_editor.export_data()]
        
        # Save to file
        filename = "level.json"
        if LevelUtils.save_level(self.current_level, filename):
            print(f"Level saved to {filename}")
    
    def _load_level(self):
        """Load level from file"""
        filename = "level.json"
        level_data = LevelUtils.load_level(filename)
        
        if level_data and LevelUtils.validate_level(level_data):
            self.current_level = level_data
            
            # Load first room if available
            if level_data.get('rooms'):
                self.room_editor.import_data(level_data['rooms'][0])
            
            print(f"Level loaded from {filename}")
    
    def _undo(self):
        """Undo last action"""
        action = self.history.undo()
        if action:
            # TODO: Implement undo logic
            print("Undo")
    
    def _redo(self):
        """Redo last undone action"""
        action = self.history.redo()
        if action:
            # TODO: Implement redo logic
            print("Redo")
    
    def run(self):
        """Run editor main loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

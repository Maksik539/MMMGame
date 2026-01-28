"""
Tabs panel for switching between different editor views
"""
import pygame
import config
from src.editor.resizable_panel import ResizablePanel


class TabsPanel(ResizablePanel):
    """Panel with tabs for switching between views"""
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "Tabs")
        self.tabs = ["Animations", "Properties"]
        self.active_tab = "Animations"
        
    def handle_event(self, event):
        """Handle input events"""
        if super().handle_event(event):
            return True
            
        if not self.visible:
            return False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Check tab clicks
                tab_width = self.rect.width // len(self.tabs)
                for i, tab in enumerate(self.tabs):
                    tab_rect = pygame.Rect(
                        self.rect.x + i * tab_width,
                        self.rect.y + 30,
                        tab_width,
                        30
                    )
                    if tab_rect.collidepoint(event.pos):
                        self.active_tab = tab
                        return True
                        
        return False
        
    def draw(self, surface):
        """Draw the tabs panel"""
        super().draw(surface)
        
        if not self.visible:
            return
            
        # Draw tabs
        tab_width = self.rect.width // len(self.tabs)
        for i, tab in enumerate(self.tabs):
            tab_rect = pygame.Rect(
                self.rect.x + i * tab_width,
                self.rect.y + 30,
                tab_width,
                30
            )
            
            # Active tab is highlighted
            if tab == self.active_tab:
                pygame.draw.rect(surface, config.BLUE, tab_rect)
            else:
                pygame.draw.rect(surface, config.GRAY, tab_rect)
            pygame.draw.rect(surface, config.WHITE, tab_rect, 1)
            
            # Tab text
            text_surface = self.font.render(tab, True, config.WHITE)
            text_rect = text_surface.get_rect(center=tab_rect.center)
            surface.blit(text_surface, text_rect)
            
    def get_active_tab(self):
        """Get the currently active tab"""
        return self.active_tab

"""
Tabs Panel
"""
import pygame
from config import *


class TabsPanel:
    """Panel with tabs for different editing modes"""
    
    def __init__(self, x, y, width, height):
        """Initialize tabs panel"""
        self.rect = pygame.Rect(x, y, width, height)
        self.tabs = ["Tiles", "Objects", "Enemies", "Items"]
        self.active_tab = 0
    
    def handle_event(self, event):
        """Handle panel events"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self._check_tab_click(event.pos)
    
    def _check_tab_click(self, pos):
        """Check if a tab was clicked"""
        if not self.rect.collidepoint(pos):
            return
        
        tab_width = self.rect.width // len(self.tabs)
        relative_x = pos[0] - self.rect.x
        
        for i in range(len(self.tabs)):
            if i * tab_width <= relative_x < (i + 1) * tab_width:
                self.active_tab = i
                break
    
    def get_active_tab(self):
        """Get currently active tab"""
        return self.tabs[self.active_tab]
    
    def draw(self, surface):
        """Draw tabs panel"""
        tab_width = self.rect.width // len(self.tabs)
        tab_height = 30
        
        # Draw tabs
        for i, tab in enumerate(self.tabs):
            x = self.rect.x + i * tab_width
            y = self.rect.y
            
            # Tab background
            if i == self.active_tab:
                color = (60, 60, 60)
            else:
                color = (40, 40, 40)
            
            tab_rect = pygame.Rect(x, y, tab_width, tab_height)
            pygame.draw.rect(surface, color, tab_rect)
            pygame.draw.rect(surface, (80, 80, 80), tab_rect, 1)
            
            # Tab text
            font = pygame.font.Font(None, 20)
            text = font.render(tab, True, WHITE)
            text_rect = text.get_rect(center=(x + tab_width // 2, y + tab_height // 2))
            surface.blit(text, text_rect)

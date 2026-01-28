"""
Minimap Panel
"""
import pygame
from config import *


class MinimapPanel:
    """Panel showing minimap of the level"""
    
    def __init__(self, x, y, width, height):
        """Initialize minimap panel"""
        self.rect = pygame.Rect(x, y, width, height)
        self.zoom = 0.1
        self.offset_x = 0
        self.offset_y = 0
    
    def set_zoom(self, zoom):
        """Set minimap zoom level"""
        self.zoom = max(0.05, min(1.0, zoom))
    
    def handle_event(self, event):
        """Handle panel events"""
        if event.type == pygame.MOUSEWHEEL:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.zoom += event.y * 0.05
                self.zoom = max(0.05, min(1.0, self.zoom))
    
    def draw(self, surface, level_data=None):
        """Draw minimap panel"""
        # Draw background
        pygame.draw.rect(surface, (30, 30, 30), self.rect)
        
        # Draw title
        font = pygame.font.Font(None, 20)
        title = font.render("Minimap", True, WHITE)
        surface.blit(title, (self.rect.x + 5, self.rect.y + 5))
        
        # Draw minimap content
        content_rect = pygame.Rect(
            self.rect.x + 5,
            self.rect.y + 25,
            self.rect.width - 10,
            self.rect.height - 30
        )
        pygame.draw.rect(surface, BLACK, content_rect)
        
        # Draw level data if available
        if level_data:
            # TODO: Implement minimap rendering
            pass
        
        # Draw border
        pygame.draw.rect(surface, (80, 80, 80), self.rect, 1)
        pygame.draw.rect(surface, (60, 60, 60), content_rect, 1)

"""
Properties Panel
"""
import pygame
from config import *


class PropertiesPanel:
    """Panel for editing object properties"""
    
    def __init__(self, x, y, width, height):
        """Initialize properties panel"""
        self.rect = pygame.Rect(x, y, width, height)
        self.selected_object = None
        self.properties = {}
    
    def set_selected_object(self, obj, properties):
        """Set currently selected object and its properties"""
        self.selected_object = obj
        self.properties = properties.copy() if properties else {}
    
    def handle_event(self, event):
        """Handle panel events"""
        # TODO: Implement property editing
        pass
    
    def draw(self, surface):
        """Draw properties panel"""
        # Draw background
        pygame.draw.rect(surface, (40, 40, 40), self.rect)
        
        # Draw title
        font = pygame.font.Font(None, 24)
        title = font.render("Properties", True, WHITE)
        surface.blit(title, (self.rect.x + 5, self.rect.y + 5))
        
        # Draw properties
        if self.properties:
            y_offset = self.rect.y + 35
            for key, value in self.properties.items():
                text = font.render(f"{key}: {value}", True, WHITE)
                surface.blit(text, (self.rect.x + 10, y_offset))
                y_offset += 25
        else:
            no_sel = font.render("No selection", True, GRAY)
            surface.blit(no_sel, (self.rect.x + 10, self.rect.y + 35))
        
        # Draw border
        pygame.draw.rect(surface, (80, 80, 80), self.rect, 1)

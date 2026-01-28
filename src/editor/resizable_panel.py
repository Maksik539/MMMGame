"""
Resizable Panel Base Class
"""
import pygame
from config import *


class ResizablePanel:
    """Base class for resizable panels"""
    
    def __init__(self, x, y, width, height, title="Panel"):
        """Initialize resizable panel"""
        self.rect = pygame.Rect(x, y, width, height)
        self.title = title
        self.is_resizing = False
        self.resize_edge = None
        self.min_width = 100
        self.min_height = 50
        self.border_size = 5
        
        # Colors
        self.bg_color = (40, 40, 40)
        self.border_color = (80, 80, 80)
        self.title_color = (60, 60, 60)
        self.text_color = WHITE
    
    def handle_event(self, event):
        """Handle panel events"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                edge = self._get_resize_edge(mouse_pos)
                if edge:
                    self.is_resizing = True
                    self.resize_edge = edge
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.is_resizing = False
                self.resize_edge = None
        
        elif event.type == pygame.MOUSEMOTION:
            if self.is_resizing and self.resize_edge:
                self._resize(event.pos)
    
    def _get_resize_edge(self, pos):
        """Check if mouse is on resize edge"""
        x, y = pos
        rect = self.rect
        
        # Check edges
        if abs(x - rect.right) < self.border_size and rect.top < y < rect.bottom:
            return "right"
        elif abs(y - rect.bottom) < self.border_size and rect.left < x < rect.right:
            return "bottom"
        
        return None
    
    def _resize(self, pos):
        """Resize panel"""
        x, y = pos
        
        if self.resize_edge == "right":
            new_width = max(self.min_width, x - self.rect.left)
            self.rect.width = new_width
        elif self.resize_edge == "bottom":
            new_height = max(self.min_height, y - self.rect.top)
            self.rect.height = new_height
    
    def draw(self, surface):
        """Draw panel"""
        # Draw background
        pygame.draw.rect(surface, self.bg_color, self.rect)
        
        # Draw title bar
        title_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 25)
        pygame.draw.rect(surface, self.title_color, title_rect)
        
        # Draw title text
        font = pygame.font.Font(None, 20)
        title_text = font.render(self.title, True, self.text_color)
        surface.blit(title_text, (self.rect.x + 5, self.rect.y + 5))
        
        # Draw border
        pygame.draw.rect(surface, self.border_color, self.rect, 1)
    
    def contains_point(self, pos):
        """Check if point is inside panel"""
        return self.rect.collidepoint(pos)

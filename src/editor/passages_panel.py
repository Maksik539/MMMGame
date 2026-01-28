"""
Passages Panel
"""
import pygame
from config import *


class PassagesPanel:
    """Panel for managing room passages/doors"""
    
    def __init__(self, x, y, width, height):
        """Initialize passages panel"""
        self.rect = pygame.Rect(x, y, width, height)
        self.passages = []
        self.selected_passage = None
    
    def add_passage(self, x, y, direction, target_room=None):
        """Add passage at position"""
        passage = {
            'x': x,
            'y': y,
            'direction': direction,
            'target': target_room
        }
        self.passages.append(passage)
    
    def remove_passage(self, index):
        """Remove passage by index"""
        if 0 <= index < len(self.passages):
            self.passages.pop(index)
    
    def handle_event(self, event):
        """Handle panel events"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if event.button == 1:
                    self._select_passage(event.pos)
    
    def _select_passage(self, pos):
        """Select passage at position"""
        relative_y = pos[1] - self.rect.y - 30
        
        if relative_y < 0:
            return
        
        index = relative_y // 25
        
        if 0 <= index < len(self.passages):
            self.selected_passage = index
    
    def draw(self, surface):
        """Draw passages panel"""
        # Draw background
        pygame.draw.rect(surface, (40, 40, 40), self.rect)
        
        # Draw title
        font = pygame.font.Font(None, 24)
        title = font.render("Passages", True, WHITE)
        surface.blit(title, (self.rect.x + 5, self.rect.y + 5))
        
        # Draw passages list
        y_offset = self.rect.y + 30
        
        for i, passage in enumerate(self.passages):
            y = y_offset + i * 25
            
            if y > self.rect.bottom - 25:
                break
            
            # Highlight selected
            color = GREEN if i == self.selected_passage else WHITE
            text = font.render(
                f"{passage['direction']} at ({passage['x']}, {passage['y']})",
                True,
                color
            )
            surface.blit(text, (self.rect.x + 10, y))
        
        # Draw border
        pygame.draw.rect(surface, (80, 80, 80), self.rect, 1)

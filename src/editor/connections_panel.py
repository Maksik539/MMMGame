"""
Connections Panel
"""
import pygame
from config import *


class ConnectionsPanel:
    """Panel for managing room connections"""
    
    def __init__(self, x, y, width, height):
        """Initialize connections panel"""
        self.rect = pygame.Rect(x, y, width, height)
        self.connections = []
        self.selected_connection = None
    
    def add_connection(self, from_room, to_room, connection_type="door"):
        """Add connection between rooms"""
        connection = {
            'from': from_room,
            'to': to_room,
            'type': connection_type
        }
        self.connections.append(connection)
    
    def remove_connection(self, index):
        """Remove connection by index"""
        if 0 <= index < len(self.connections):
            self.connections.pop(index)
    
    def handle_event(self, event):
        """Handle panel events"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if event.button == 1:
                    self._select_connection(event.pos)
    
    def _select_connection(self, pos):
        """Select connection at position"""
        relative_y = pos[1] - self.rect.y - 30
        
        if relative_y < 0:
            return
        
        index = relative_y // 25
        
        if 0 <= index < len(self.connections):
            self.selected_connection = index
    
    def draw(self, surface):
        """Draw connections panel"""
        # Draw background
        pygame.draw.rect(surface, (40, 40, 40), self.rect)
        
        # Draw title
        font = pygame.font.Font(None, 24)
        title = font.render("Connections", True, WHITE)
        surface.blit(title, (self.rect.x + 5, self.rect.y + 5))
        
        # Draw connections list
        y_offset = self.rect.y + 30
        
        for i, conn in enumerate(self.connections):
            y = y_offset + i * 25
            
            if y > self.rect.bottom - 25:
                break
            
            # Highlight selected
            color = GREEN if i == self.selected_connection else WHITE
            text = font.render(f"{conn['from']} -> {conn['to']}", True, color)
            surface.blit(text, (self.rect.x + 10, y))
        
        # Draw border
        pygame.draw.rect(surface, (80, 80, 80), self.rect, 1)

"""
Connections panel for managing room connections
"""
import pygame
import config
from src.editor.resizable_panel import ResizablePanel


class ConnectionsPanel(ResizablePanel):
    """Panel for managing connections between rooms"""
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "Connections")
        self.connections = []
        
    def add_connection(self, room1, room2, direction):
        """Add a connection between rooms"""
        self.connections.append({
            "room1": room1,
            "room2": room2,
            "direction": direction
        })
        
    def remove_connection(self, index):
        """Remove a connection"""
        if 0 <= index < len(self.connections):
            self.connections.pop(index)
            
    def draw(self, surface):
        """Draw the connections panel"""
        super().draw(surface)
        
        if not self.visible:
            return
            
        y_offset = 40
        
        if not self.connections:
            text = self.font.render("No connections", True, config.WHITE)
            surface.blit(text, (self.rect.x + 10, self.rect.y + y_offset))
        else:
            for i, conn in enumerate(self.connections):
                text = self.font.render(
                    f"{conn['room1']} -> {conn['room2']} ({conn['direction']})",
                    True, config.WHITE
                )
                surface.blit(text, (self.rect.x + 10, self.rect.y + y_offset + i * 25))
                
    def get_connections(self):
        """Get all connections"""
        return self.connections.copy()

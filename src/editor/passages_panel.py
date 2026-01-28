"""
Passages panel for managing level transitions
"""
import pygame
import config
from src.editor.resizable_panel import ResizablePanel


class PassagesPanel(ResizablePanel):
    """Panel for managing passages between levels"""
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "Passages")
        self.passages = []
        
    def add_passage(self, position, target_level, target_position):
        """Add a passage to another level"""
        self.passages.append({
            "position": position,
            "target_level": target_level,
            "target_position": target_position
        })
        
    def remove_passage(self, index):
        """Remove a passage"""
        if 0 <= index < len(self.passages):
            self.passages.pop(index)
            
    def draw(self, surface):
        """Draw the passages panel"""
        super().draw(surface)
        
        if not self.visible:
            return
            
        y_offset = 40
        
        if not self.passages:
            text = self.font.render("No passages", True, config.WHITE)
            surface.blit(text, (self.rect.x + 10, self.rect.y + y_offset))
        else:
            for i, passage in enumerate(self.passages):
                pos = passage['position']
                target = passage['target_level']
                text = self.font.render(
                    f"({pos[0]},{pos[1]}) -> {target}",
                    True, config.WHITE
                )
                surface.blit(text, (self.rect.x + 10, self.rect.y + y_offset + i * 25))
                
    def get_passages(self):
        """Get all passages"""
        return self.passages.copy()

"""
Properties panel for editing object properties
"""
import pygame
import config
from src.editor.resizable_panel import ResizablePanel


class PropertiesPanel(ResizablePanel):
    """Panel for editing properties of selected objects"""
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "Properties")
        self.properties = {}
        self.selected_object = None
        
    def set_object(self, obj, properties):
        """Set the object to edit"""
        self.selected_object = obj
        self.properties = properties.copy()
        
    def clear(self):
        """Clear selected object"""
        self.selected_object = None
        self.properties = {}
        
    def draw(self, surface):
        """Draw the properties panel"""
        super().draw(surface)
        
        if not self.visible:
            return
            
        y_offset = 35
        
        if not self.selected_object:
            # No object selected
            text = self.font.render("No object selected", True, config.WHITE)
            surface.blit(text, (self.rect.x + 10, self.rect.y + y_offset))
        else:
            # Draw properties
            for i, (key, value) in enumerate(self.properties.items()):
                text = self.font.render(f"{key}: {value}", True, config.WHITE)
                surface.blit(text, (self.rect.x + 10, self.rect.y + y_offset + i * 25))
                
    def get_properties(self):
        """Get current properties"""
        return self.properties.copy()

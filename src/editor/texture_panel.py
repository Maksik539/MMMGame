"""
Texture panel for selecting tiles in the level editor
"""
import pygame
import config
from src.editor.resizable_panel import ResizablePanel


class TexturePanel(ResizablePanel):
    """Panel for selecting textures/tiles"""
    
    def __init__(self, x, y, width, height, texture_loader):
        super().__init__(x, y, width, height, "Textures")
        self.texture_loader = texture_loader
        self.selected_texture = None
        self.texture_list = ["floor", "wall", "door"]
        
        # Load all textures
        for name in self.texture_list:
            self.texture_loader.load_texture(name)
            
    def handle_event(self, event):
        """Handle input events"""
        if super().handle_event(event):
            return True
            
        if not self.visible:
            return False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Check if clicking on a texture
                if self.rect.collidepoint(event.pos):
                    relative_y = event.pos[1] - self.rect.y - 35
                    index = relative_y // 40
                    if 0 <= index < len(self.texture_list):
                        self.selected_texture = self.texture_list[index]
                        return True
                        
        return False
        
    def draw(self, surface):
        """Draw the texture panel"""
        super().draw(surface)
        
        if not self.visible:
            return
            
        # Draw texture list
        y_offset = 35
        for i, name in enumerate(self.texture_list):
            texture = self.texture_loader.get_texture(name)
            
            # Background for texture item
            item_rect = pygame.Rect(
                self.rect.x + 5,
                self.rect.y + y_offset + i * 40,
                self.rect.width - 10,
                35
            )
            
            # Highlight selected
            if name == self.selected_texture:
                pygame.draw.rect(surface, config.BLUE, item_rect)
            else:
                pygame.draw.rect(surface, config.GRAY, item_rect)
            pygame.draw.rect(surface, config.WHITE, item_rect, 1)
            
            # Draw texture preview (scaled up)
            scaled_texture = pygame.transform.scale(texture, (32, 32))
            surface.blit(scaled_texture, (self.rect.x + 10, self.rect.y + y_offset + i * 40 + 2))
            
            # Draw name
            name_surface = self.font.render(name, True, config.WHITE)
            surface.blit(name_surface, (self.rect.x + 50, self.rect.y + y_offset + i * 40 + 8))
            
    def get_selected_texture(self):
        """Get the currently selected texture"""
        return self.selected_texture

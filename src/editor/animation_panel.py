"""
Animation panel for selecting animations in the level editor
"""
import pygame
import config
from src.editor.resizable_panel import ResizablePanel


class AnimationPanel(ResizablePanel):
    """Panel for selecting animations"""
    
    def __init__(self, x, y, width, height, animation_loader):
        super().__init__(x, y, width, height, "Animations")
        self.animation_loader = animation_loader
        self.selected_animation = None
        
    def handle_event(self, event):
        """Handle input events"""
        if super().handle_event(event):
            return True
            
        if not self.visible:
            return False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    animations = self.animation_loader.get_all_animations()
                    relative_y = event.pos[1] - self.rect.y - 35
                    index = relative_y // 30
                    if 0 <= index < len(animations):
                        self.selected_animation = animations[index]
                        return True
                        
        return False
        
    def draw(self, surface):
        """Draw the animation panel"""
        super().draw(surface)
        
        if not self.visible:
            return
            
        # Draw animation list
        animations = self.animation_loader.get_all_animations()
        y_offset = 35
        
        for i, name in enumerate(animations):
            item_rect = pygame.Rect(
                self.rect.x + 5,
                self.rect.y + y_offset + i * 30,
                self.rect.width - 10,
                25
            )
            
            # Highlight selected
            if name == self.selected_animation:
                pygame.draw.rect(surface, config.BLUE, item_rect)
            else:
                pygame.draw.rect(surface, config.GRAY, item_rect)
            pygame.draw.rect(surface, config.WHITE, item_rect, 1)
            
            # Draw name
            name_surface = self.font.render(name, True, config.WHITE)
            surface.blit(name_surface, (self.rect.x + 10, self.rect.y + y_offset + i * 30 + 4))
            
    def get_selected_animation(self):
        """Get the currently selected animation"""
        return self.selected_animation

"""
Animation Panel
"""
import pygame
from config import *
from src.editor.animation_loader import animation_loader


class AnimationPanel:
    """Panel for managing animations"""
    
    def __init__(self, x, y, width, height):
        """Initialize animation panel"""
        self.rect = pygame.Rect(x, y, width, height)
        self.selected_animation = None
        self.scroll_offset = 0
    
    def handle_event(self, event):
        """Handle panel events"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if event.button == 1:  # Left click
                    self._select_animation(event.pos)
                elif event.button == 4:  # Scroll up
                    self.scroll_offset = max(0, self.scroll_offset - 1)
                elif event.button == 5:  # Scroll down
                    animations = animation_loader.get_all_animations()
                    max_scroll = max(0, len(animations) - (self.rect.height - 30) // 30)
                    self.scroll_offset = min(max_scroll, self.scroll_offset + 1)
    
    def _select_animation(self, pos):
        """Select animation at position"""
        relative_y = pos[1] - self.rect.y - 30
        
        if relative_y < 0:
            return
        
        animations = animation_loader.get_all_animations()
        index = (relative_y // 30) + self.scroll_offset
        
        if 0 <= index < len(animations):
            self.selected_animation = animations[index]
    
    def get_selected_animation(self):
        """Get currently selected animation"""
        return self.selected_animation
    
    def draw(self, surface):
        """Draw animation panel"""
        # Draw background
        pygame.draw.rect(surface, (40, 40, 40), self.rect)
        
        # Draw title
        font = pygame.font.Font(None, 24)
        title = font.render("Animations", True, WHITE)
        surface.blit(title, (self.rect.x + 5, self.rect.y + 5))
        
        # Draw animations list
        animations = animation_loader.get_all_animations()
        y_offset = self.rect.y + 30
        
        for i, anim_name in enumerate(animations):
            row = i - self.scroll_offset
            
            if row < 0:
                continue
            
            y = y_offset + row * 30
            
            if y > self.rect.bottom - 30:
                break
            
            # Highlight selected
            color = GREEN if anim_name == self.selected_animation else WHITE
            text = font.render(anim_name, True, color)
            surface.blit(text, (self.rect.x + 10, y))
        
        # Draw border
        pygame.draw.rect(surface, (80, 80, 80), self.rect, 1)

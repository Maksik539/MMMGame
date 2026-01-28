"""
Base class for resizable panels in the editor
"""
import pygame
import config


class ResizablePanel:
    """Base class for resizable UI panels"""
    
    def __init__(self, x, y, width, height, title="Panel"):
        self.rect = pygame.Rect(x, y, width, height)
        self.title = title
        self.is_dragging = False
        self.is_resizing = False
        self.drag_offset = (0, 0)
        self.min_width = 100
        self.min_height = 100
        self.resize_handle_size = 10
        self.visible = True
        
        # Fonts
        self.title_font = pygame.font.Font(None, 24)
        self.font = pygame.font.Font(None, 20)
        
    def get_resize_handle_rect(self):
        """Get the rect for the resize handle"""
        return pygame.Rect(
            self.rect.right - self.resize_handle_size,
            self.rect.bottom - self.resize_handle_size,
            self.resize_handle_size,
            self.resize_handle_size
        )
        
    def handle_event(self, event):
        """Handle input events"""
        if not self.visible:
            return False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Check resize handle
                resize_rect = self.get_resize_handle_rect()
                if resize_rect.collidepoint(event.pos):
                    self.is_resizing = True
                    return True
                    
                # Check title bar for dragging
                title_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 30)
                if title_rect.collidepoint(event.pos):
                    self.is_dragging = True
                    self.drag_offset = (
                        event.pos[0] - self.rect.x,
                        event.pos[1] - self.rect.y
                    )
                    return True
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.is_dragging = False
                self.is_resizing = False
                
        elif event.type == pygame.MOUSEMOTION:
            if self.is_dragging:
                self.rect.x = event.pos[0] - self.drag_offset[0]
                self.rect.y = event.pos[1] - self.drag_offset[1]
                return True
            elif self.is_resizing:
                new_width = max(self.min_width, event.pos[0] - self.rect.x)
                new_height = max(self.min_height, event.pos[1] - self.rect.y)
                self.rect.width = new_width
                self.rect.height = new_height
                return True
                
        return False
        
    def draw(self, surface):
        """Draw the panel"""
        if not self.visible:
            return
            
        # Background
        pygame.draw.rect(surface, config.DARK_GRAY, self.rect)
        pygame.draw.rect(surface, config.WHITE, self.rect, 2)
        
        # Title bar
        title_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 30)
        pygame.draw.rect(surface, config.GRAY, title_rect)
        pygame.draw.rect(surface, config.WHITE, title_rect, 1)
        
        # Title text
        title_surface = self.title_font.render(self.title, True, config.WHITE)
        surface.blit(title_surface, (self.rect.x + 5, self.rect.y + 5))
        
        # Resize handle
        resize_rect = self.get_resize_handle_rect()
        pygame.draw.rect(surface, config.WHITE, resize_rect)
        
    def update(self):
        """Update panel state"""
        pass

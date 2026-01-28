"""
Minimap panel showing overview of rooms
"""
import pygame
import config
from src.editor.resizable_panel import ResizablePanel


class MinimapPanel(ResizablePanel):
    """Panel showing a minimap of the level"""
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "Minimap")
        self.level_data = None
        
    def set_level(self, level_data):
        """Set the level to display"""
        self.level_data = level_data
        
    def draw(self, surface):
        """Draw the minimap panel"""
        super().draw(surface)
        
        if not self.visible:
            return
            
        if not self.level_data:
            text = self.font.render("No level loaded", True, config.WHITE)
            surface.blit(text, (self.rect.x + 10, self.rect.y + 40))
            return
            
        # Draw simplified minimap
        content_rect = pygame.Rect(
            self.rect.x + 10,
            self.rect.y + 40,
            self.rect.width - 20,
            self.rect.height - 60
        )
        
        # Calculate scale
        level_width = self.level_data.get("width", 1)
        level_height = self.level_data.get("height", 1)
        
        scale_x = content_rect.width / level_width
        scale_y = content_rect.height / level_height
        scale = min(scale_x, scale_y, 4)  # Max 4 pixels per tile
        
        # Draw tiles
        tiles = self.level_data.get("tiles", [])
        for y, row in enumerate(tiles):
            for x, tile in enumerate(row):
                if tile != 0:  # Don't draw empty tiles
                    tile_rect = pygame.Rect(
                        content_rect.x + x * scale,
                        content_rect.y + y * scale,
                        max(1, scale),
                        max(1, scale)
                    )
                    # Simple color coding
                    color = config.WHITE if tile == "wall" else config.GRAY
                    pygame.draw.rect(surface, color, tile_rect)

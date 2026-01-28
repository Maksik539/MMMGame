"""
Room editor for editing individual rooms
"""
import pygame
import config


class RoomEditor:
    """Editor for individual rooms in the level"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[0 for _ in range(width)] for _ in range(height)]
        self.camera_x = 0
        self.camera_y = 0
        self.zoom = 1.0
        self.selected_tile = None
        
    def set_tile(self, x, y, tile_id):
        """Set a tile at position"""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.tiles[y][x] = tile_id
            
    def get_tile(self, x, y):
        """Get tile at position"""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        return None
        
    def handle_event(self, event, editor_rect):
        """Handle input events"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and editor_rect.collidepoint(event.pos):
                # Paint tile
                grid_x, grid_y = self.screen_to_grid(
                    event.pos[0] - editor_rect.x,
                    event.pos[1] - editor_rect.y
                )
                if self.selected_tile:
                    self.set_tile(grid_x, grid_y, self.selected_tile)
                return True
                    
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] and editor_rect.collidepoint(event.pos):
                # Continue painting while dragging
                grid_x, grid_y = self.screen_to_grid(
                    event.pos[0] - editor_rect.x,
                    event.pos[1] - editor_rect.y
                )
                if self.selected_tile:
                    self.set_tile(grid_x, grid_y, self.selected_tile)
                return True
                
        return False
        
    def screen_to_grid(self, screen_x, screen_y):
        """Convert screen coordinates to grid coordinates"""
        tile_size = int(config.TILE_SIZE * self.zoom)
        grid_x = (screen_x + self.camera_x) // tile_size
        grid_y = (screen_y + self.camera_y) // tile_size
        return grid_x, grid_y
        
    def draw(self, surface, rect, texture_loader):
        """Draw the room editor"""
        # Clip to editor area
        surface.set_clip(rect)
        
        tile_size = int(config.TILE_SIZE * self.zoom)
        
        # Draw grid and tiles
        for y in range(self.height):
            for x in range(self.width):
                screen_x = rect.x + x * tile_size - self.camera_x
                screen_y = rect.y + y * tile_size - self.camera_y
                
                # Skip if outside visible area
                if (screen_x + tile_size < rect.x or screen_x > rect.right or
                    screen_y + tile_size < rect.y or screen_y > rect.bottom):
                    continue
                    
                # Draw tile
                tile_id = self.tiles[y][x]
                if tile_id and tile_id != 0:
                    texture = texture_loader.get_texture(tile_id)
                    if texture:
                        scaled = pygame.transform.scale(texture, (tile_size, tile_size))
                        surface.blit(scaled, (screen_x, screen_y))
                        
                # Draw grid
                pygame.draw.rect(
                    surface, config.DARK_GRAY,
                    (screen_x, screen_y, tile_size, tile_size),
                    1
                )
                
        # Reset clip
        surface.set_clip(None)
        
    def get_room_data(self):
        """Get room data for saving"""
        return {
            "width": self.width,
            "height": self.height,
            "tiles": self.tiles
        }
        
    def load_room_data(self, data):
        """Load room data"""
        self.width = data.get("width", self.width)
        self.height = data.get("height", self.height)
        self.tiles = data.get("tiles", self.tiles)

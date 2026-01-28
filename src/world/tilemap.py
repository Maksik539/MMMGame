"""
Tilemap and Level Builder
"""
import pygame
from config import *
from src.graphics.asset_coordinator import asset_coordinator
from src.graphics.procedural_sprites import ProceduralSpriteGenerator


class Tile:
    """Individual tile class"""
    
    def __init__(self, x, y, tile_type="ground"):
        """Initialize tile"""
        self.x = x
        self.y = y
        self.tile_type = tile_type
        
        # Graphics
        sprite_gen = ProceduralSpriteGenerator()
        self.image = sprite_gen.generate_tile_sprite(TILE_SIZE, TILE_SIZE)
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
    
    def draw(self, surface, camera_x=0, camera_y=0):
        """Draw tile"""
        surface.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))


class LevelBuilder:
    """Builds and manages game levels"""
    
    def __init__(self):
        """Initialize level builder"""
        self.tiles = []
        self.width = 0
        self.height = 0
    
    def add_tile(self, x, y, tile_type="ground"):
        """Add tile to level"""
        tile = Tile(x, y, tile_type)
        self.tiles.append(tile)
        
        # Update level dimensions
        self.width = max(self.width, x + TILE_SIZE)
        self.height = max(self.height, y + TILE_SIZE)
        
        return tile
    
    def remove_tile(self, x, y):
        """Remove tile at position"""
        self.tiles = [t for t in self.tiles if not (t.x == x and t.y == y)]
    
    def get_tile_at(self, x, y):
        """Get tile at position"""
        for tile in self.tiles:
            if tile.x == x and tile.y == y:
                return tile
        return None
    
    def get_tiles(self):
        """Get all tiles"""
        return self.tiles
    
    def load_from_file(self, filename):
        """Load level from file"""
        # TODO: Implement level loading
        pass
    
    def save_to_file(self, filename):
        """Save level to file"""
        # TODO: Implement level saving
        pass
    
    def draw(self, surface, camera_x=0, camera_y=0):
        """Draw all tiles"""
        for tile in self.tiles:
            # Only draw tiles visible on screen
            if (tile.rect.x - camera_x < SCREEN_WIDTH and
                tile.rect.x - camera_x + TILE_SIZE > 0 and
                tile.rect.y - camera_y < SCREEN_HEIGHT and
                tile.rect.y - camera_y + TILE_SIZE > 0):
                tile.draw(surface, camera_x, camera_y)
    
    def clear(self):
        """Clear all tiles"""
        self.tiles.clear()
        self.width = 0
        self.height = 0

"""
Tilemap and level building system for Mage Quest
"""
import pygame
import json
import os
import random
import config


class TileMap:
    """Manages tile-based maps"""
    
    def __init__(self, width, height, tileset):
        self.width = width
        self.height = height
        self.tileset = tileset
        self.tiles = [[0 for _ in range(width)] for _ in range(height)]
        
    def set_tile(self, x, y, tile_id):
        """Set a tile at the given position"""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.tiles[y][x] = tile_id
            
    def get_tile(self, x, y):
        """Get tile at the given position"""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        return None
        
    def draw(self, surface, camera_offset=(0, 0)):
        """Draw the tilemap"""
        for y in range(self.height):
            for x in range(self.width):
                tile_id = self.tiles[y][x]
                if tile_id in self.tileset:
                    tile_sprite = self.tileset[tile_id]
                    pos = (
                        x * config.TILE_SIZE - camera_offset[0],
                        y * config.TILE_SIZE - camera_offset[1]
                    )
                    surface.blit(tile_sprite, pos)
                    
    def save(self, filename):
        """Save tilemap to JSON file"""
        data = {
            "width": self.width,
            "height": self.height,
            "tiles": self.tiles
        }
        filepath = os.path.join(config.LEVELS_DIR, filename)
        with open(filepath, 'w') as f:
            json.dump(data, f)
            
    @classmethod
    def load(cls, filename, tileset):
        """Load tilemap from JSON file"""
        filepath = os.path.join(config.LEVELS_DIR, filename)
        if not os.path.exists(filepath):
            return None
            
        with open(filepath, 'r') as f:
            data = json.load(f)
            
        tilemap = cls(data["width"], data["height"], tileset)
        tilemap.tiles = data["tiles"]
        return tilemap


class LevelBuilder:
    """Procedurally builds dungeon levels"""
    
    def __init__(self, tileset):
        self.tileset = tileset
        
    def generate_room(self, width, height):
        """Generate a simple rectangular room"""
        tilemap = TileMap(width, height, self.tileset)
        
        for y in range(height):
            for x in range(width):
                # Walls on edges
                if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                    tilemap.set_tile(x, y, "wall")
                else:
                    tilemap.set_tile(x, y, "floor")
                    
        return tilemap
        
    def generate_dungeon(self, num_rooms=5):
        """Generate a simple dungeon with multiple rooms"""
        # For now, just generate a single large room
        # This can be expanded to create more complex dungeons
        return self.generate_room(50, 40)
        
    def add_doors(self, tilemap):
        """Add doors to walls"""
        # Find suitable wall positions and add doors
        for y in range(1, tilemap.height - 1):
            for x in range(1, tilemap.width - 1):
                if tilemap.get_tile(x, y) == "wall":
                    # Check if this could be a door (has floor on both sides)
                    if (tilemap.get_tile(x - 1, y) == "floor" and 
                        tilemap.get_tile(x + 1, y) == "floor"):
                        if random.random() < 0.1:  # 10% chance
                            tilemap.set_tile(x, y, "door")
                    elif (tilemap.get_tile(x, y - 1) == "floor" and 
                          tilemap.get_tile(x, y + 1) == "floor"):
                        if random.random() < 0.1:  # 10% chance
                            tilemap.set_tile(x, y, "door")
        
        return tilemap

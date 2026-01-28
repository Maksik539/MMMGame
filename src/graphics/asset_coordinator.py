"""
Asset coordinator for managing game assets
"""
import pygame
import os
import config
from src.graphics.procedural_sprites import ProceduralSpriteGenerator


class AssetCoordinator:
    """Coordinates loading and management of game assets"""
    
    def __init__(self):
        self.sprites = {}
        self.tilesets = {}
        self.generator = ProceduralSpriteGenerator()
        
    def load_sprite(self, name, filename=None):
        """Load a sprite from file or generate it procedurally"""
        if filename and os.path.exists(os.path.join(config.SPRITES_DIR, filename)):
            # Load from file
            sprite = pygame.image.load(os.path.join(config.SPRITES_DIR, filename))
            self.sprites[name] = sprite
        else:
            # Generate procedurally
            if name == "mage":
                sprite = self.generator.generate_mage_sprite()
            elif name == "skeleton":
                sprite = self.generator.generate_skeleton_sprite()
            elif name == "fire_sphere":
                sprite = self.generator.generate_fire_sphere_sprite()
            elif name == "tornado":
                sprite = self.generator.generate_tornado_sprite()
            elif name.startswith("projectile"):
                sprite = self.generator.generate_projectile_sprite()
            else:
                # Default sprite
                sprite = pygame.Surface((16, 16))
                sprite.fill((255, 0, 255))  # Magenta for missing sprites
                
            self.sprites[name] = sprite
            
        return self.sprites[name]
        
    def load_tileset(self, name, filename=None):
        """Load a tileset from file or generate it procedurally"""
        tileset = {}
        
        if filename and os.path.exists(os.path.join(config.TILESETS_DIR, filename)):
            # Load from file (tileset image)
            # This would parse a tileset image into individual tiles
            pass
        else:
            # Generate procedurally
            tileset["floor"] = self.generator.generate_tile_sprite("floor")
            tileset["wall"] = self.generator.generate_tile_sprite("wall")
            tileset["door"] = self.generator.generate_tile_sprite("door")
            
        self.tilesets[name] = tileset
        return tileset
        
    def get_sprite(self, name):
        """Get a loaded sprite"""
        if name not in self.sprites:
            self.load_sprite(name)
        return self.sprites[name]
        
    def get_tileset(self, name):
        """Get a loaded tileset"""
        if name not in self.tilesets:
            self.load_tileset(name)
        return self.tilesets[name]
        
    def preload_common_assets(self):
        """Preload commonly used assets"""
        # Player
        self.load_sprite("mage")
        
        # Enemies
        self.load_sprite("skeleton")
        self.load_sprite("fire_sphere")
        self.load_sprite("tornado")
        
        # Projectiles
        self.load_sprite("projectile_player")
        self.load_sprite("projectile_enemy")
        
        # Tilesets
        self.load_tileset("dungeon")

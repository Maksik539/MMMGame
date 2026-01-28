"""
Texture loader for the level editor
"""
import pygame
import os
import config
from src.graphics.procedural_sprites import ProceduralSpriteGenerator


class TextureLoader:
    """Dynamically loads and caches textures"""
    
    def __init__(self):
        self.textures = {}
        self.generator = ProceduralSpriteGenerator()
        
    def load_texture(self, name, filepath=None):
        """Load a texture from file or generate it"""
        if name in self.textures:
            return self.textures[name]
            
        if filepath and os.path.exists(filepath):
            texture = pygame.image.load(filepath)
        else:
            # Generate procedurally based on name
            if name == "floor":
                texture = self.generator.generate_tile_sprite("floor")
            elif name == "wall":
                texture = self.generator.generate_tile_sprite("wall")
            elif name == "door":
                texture = self.generator.generate_tile_sprite("door")
            else:
                # Default texture
                texture = pygame.Surface((16, 16))
                texture.fill((255, 0, 255))
                
        self.textures[name] = texture
        return texture
        
    def get_texture(self, name):
        """Get a cached texture"""
        if name not in self.textures:
            return self.load_texture(name)
        return self.textures[name]
        
    def get_all_textures(self):
        """Get all loaded texture names"""
        return list(self.textures.keys())

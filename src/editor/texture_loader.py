"""
Texture Loader
"""
import pygame
import os
from config import *


class TextureLoader:
    """Loads and manages textures for editor"""
    
    def __init__(self):
        """Initialize texture loader"""
        self.textures = {}
        self.texture_names = []
        self.assets_path = "assets"
    
    def load_texture(self, name, path):
        """Load texture from file"""
        try:
            full_path = os.path.join(self.assets_path, path)
            if os.path.exists(full_path):
                self.textures[name] = pygame.image.load(full_path).convert_alpha()
                if name not in self.texture_names:
                    self.texture_names.append(name)
            else:
                # Create placeholder
                self.textures[name] = pygame.Surface((TILE_SIZE, TILE_SIZE))
                self.textures[name].fill(GRAY)
                if name not in self.texture_names:
                    self.texture_names.append(name)
        except Exception as e:
            print(f"Error loading texture {name}: {e}")
    
    def get_texture(self, name):
        """Get texture by name"""
        return self.textures.get(name)
    
    def get_all_textures(self):
        """Get all loaded textures"""
        return self.texture_names
    
    def scan_assets_directory(self):
        """Scan assets directory for textures"""
        if not os.path.exists(self.assets_path):
            os.makedirs(self.assets_path)
            return
        
        for filename in os.listdir(self.assets_path):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                name = os.path.splitext(filename)[0]
                self.load_texture(name, filename)


# Global texture loader instance
texture_loader = TextureLoader()

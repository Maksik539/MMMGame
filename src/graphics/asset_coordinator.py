"""
Asset Coordinator - Manages game assets
"""
import pygame
import os
from config import *


class AssetCoordinator:
    """Coordinates loading and caching of game assets"""
    
    def __init__(self):
        """Initialize asset coordinator"""
        self.textures = {}
        self.animations = {}
        self.sounds = {}
        self.assets_path = "assets"
    
    def initialize(self):
        """Initialize asset coordinator and load default assets"""
        self._ensure_assets_directory()
    
    def _ensure_assets_directory(self):
        """Ensure assets directory exists"""
        if not os.path.exists(self.assets_path):
            os.makedirs(self.assets_path)
    
    def load_texture(self, name, path):
        """Load texture from file"""
        try:
            full_path = os.path.join(self.assets_path, path)
            if os.path.exists(full_path):
                self.textures[name] = pygame.image.load(full_path).convert_alpha()
            else:
                # Create placeholder if file doesn't exist
                self.textures[name] = pygame.Surface((TILE_SIZE, TILE_SIZE))
                self.textures[name].fill(GRAY)
        except Exception as e:
            print(f"Error loading texture {name}: {e}")
            self.textures[name] = pygame.Surface((TILE_SIZE, TILE_SIZE))
            self.textures[name].fill(GRAY)
    
    def get_texture(self, name):
        """Get cached texture"""
        return self.textures.get(name)
    
    def load_animation(self, name, frames):
        """Load animation from frames"""
        self.animations[name] = frames
    
    def get_animation(self, name):
        """Get cached animation frames"""
        return self.animations.get(name, [])
    
    def load_sound(self, name, path):
        """Load sound from file"""
        try:
            full_path = os.path.join(self.assets_path, path)
            if os.path.exists(full_path):
                self.sounds[name] = pygame.mixer.Sound(full_path)
        except Exception as e:
            print(f"Error loading sound {name}: {e}")
    
    def get_sound(self, name):
        """Get cached sound"""
        return self.sounds.get(name)
    
    def clear_cache(self):
        """Clear all cached assets"""
        self.textures.clear()
        self.animations.clear()
        self.sounds.clear()


# Global asset coordinator instance
asset_coordinator = AssetCoordinator()

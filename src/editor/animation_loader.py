"""
Animation Loader
"""
import pygame
import os
from config import *


class AnimationLoader:
    """Loads and manages animations for editor"""
    
    def __init__(self):
        """Initialize animation loader"""
        self.animations = {}
        self.animation_names = []
    
    def load_animation(self, name, frames):
        """Load animation from frames"""
        self.animations[name] = frames
        if name not in self.animation_names:
            self.animation_names.append(name)
    
    def get_animation(self, name):
        """Get animation by name"""
        return self.animations.get(name, [])
    
    def get_all_animations(self):
        """Get all loaded animations"""
        return self.animation_names
    
    def create_animation_from_files(self, name, file_paths):
        """Create animation from list of image files"""
        frames = []
        for path in file_paths:
            try:
                if os.path.exists(path):
                    frame = pygame.image.load(path).convert_alpha()
                    frames.append(frame)
            except Exception as e:
                print(f"Error loading frame {path}: {e}")
        
        if frames:
            self.load_animation(name, frames)


# Global animation loader instance
animation_loader = AnimationLoader()

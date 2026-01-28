"""
Animation loader for the level editor
"""
import json
import os
import pygame
from src.graphics.animation import Animation


class AnimationLoader:
    """Loads animations from JSON files"""
    
    def __init__(self):
        self.animations = {}
        
    def load_animation(self, name, filepath):
        """Load animation from JSON file"""
        if not os.path.exists(filepath):
            return None
            
        with open(filepath, 'r') as f:
            data = json.load(f)
            
        # Create frames (placeholder - would normally load images)
        frames = []
        for frame_data in data.get("frames", []):
            # Create placeholder frame
            frame = pygame.Surface((16, 16))
            frame.fill((255, 0, 255))
            frames.append(frame)
            
        animation = Animation(frames, data.get("frame_duration", 5))
        self.animations[name] = animation
        return animation
        
    def get_animation(self, name):
        """Get a loaded animation"""
        return self.animations.get(name)
        
    def get_all_animations(self):
        """Get all loaded animation names"""
        return list(self.animations.keys())

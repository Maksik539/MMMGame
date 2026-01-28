"""
Animation System
"""
import pygame
from config import *


class Animation:
    """Handles sprite animation"""
    
    def __init__(self, frames, frame_duration=100):
        """
        Initialize animation
        
        Args:
            frames: List of pygame surfaces
            frame_duration: Duration of each frame in milliseconds
        """
        self.frames = frames
        self.frame_duration = frame_duration
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
    
    def update(self):
        """Update animation frame"""
        if not self.frames:
            return
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.last_update = now
    
    def get_current_frame(self):
        """Get current animation frame"""
        if not self.frames:
            return None
        return self.frames[self.current_frame]
    
    def reset(self):
        """Reset animation to first frame"""
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()


class AnimationManager:
    """Manages multiple animations for an entity"""
    
    def __init__(self):
        """Initialize animation manager"""
        self.animations = {}
        self.current_animation = None
    
    def add_animation(self, name, animation):
        """Add animation to manager"""
        self.animations[name] = animation
        if self.current_animation is None:
            self.current_animation = name
    
    def set_animation(self, name):
        """Set current animation"""
        if name in self.animations and name != self.current_animation:
            self.current_animation = name
            self.animations[name].reset()
    
    def update(self):
        """Update current animation"""
        if self.current_animation:
            self.animations[self.current_animation].update()
    
    def get_current_frame(self):
        """Get current frame from active animation"""
        if self.current_animation:
            return self.animations[self.current_animation].get_current_frame()
        return None

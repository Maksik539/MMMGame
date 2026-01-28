"""
Animation system for Mage Quest
"""
import pygame


class Animation:
    """Represents a single animation with multiple frames"""
    
    def __init__(self, frames, frame_duration=5):
        """
        Args:
            frames: List of pygame.Surface objects
            frame_duration: Number of game frames to show each animation frame
        """
        self.frames = frames
        self.frame_duration = frame_duration
        self.current_frame = 0
        self.frame_timer = 0
        self.looping = True
        
    def update(self):
        """Update animation state"""
        self.frame_timer += 1
        if self.frame_timer >= self.frame_duration:
            self.frame_timer = 0
            self.current_frame += 1
            
            if self.current_frame >= len(self.frames):
                if self.looping:
                    self.current_frame = 0
                else:
                    self.current_frame = len(self.frames) - 1
                    
    def get_current_frame(self):
        """Get the current animation frame"""
        return self.frames[self.current_frame]
        
    def reset(self):
        """Reset animation to first frame"""
        self.current_frame = 0
        self.frame_timer = 0


class AnimationManager:
    """Manages multiple animations for a game object"""
    
    def __init__(self):
        self.animations = {}
        self.current_animation = None
        
    def add_animation(self, name, animation):
        """Add an animation to the manager"""
        self.animations[name] = animation
        if self.current_animation is None:
            self.current_animation = name
            
    def set_animation(self, name):
        """Switch to a different animation"""
        if name in self.animations and name != self.current_animation:
            self.current_animation = name
            self.animations[name].reset()
            
    def update(self):
        """Update current animation"""
        if self.current_animation and self.current_animation in self.animations:
            self.animations[self.current_animation].update()
            
    def get_current_frame(self):
        """Get current frame of active animation"""
        if self.current_animation and self.current_animation in self.animations:
            return self.animations[self.current_animation].get_current_frame()
        return None

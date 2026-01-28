"""
Animation Creator
"""
import pygame
from config import *


class AnimationCreator:
    """Tool for creating animations in the editor"""
    
    def __init__(self):
        """Initialize animation creator"""
        self.frames = []
        self.current_frame = 0
        self.frame_duration = 100
        self.is_playing = False
        self.last_update = 0
    
    def add_frame(self, surface):
        """Add frame to animation"""
        self.frames.append(surface.copy())
    
    def remove_frame(self, index):
        """Remove frame from animation"""
        if 0 <= index < len(self.frames):
            self.frames.pop(index)
            if self.current_frame >= len(self.frames) and len(self.frames) > 0:
                self.current_frame = len(self.frames) - 1
    
    def set_frame_duration(self, duration):
        """Set frame duration in milliseconds"""
        self.frame_duration = duration
    
    def play(self):
        """Start playing animation"""
        self.is_playing = True
        self.last_update = pygame.time.get_ticks()
    
    def pause(self):
        """Pause animation playback"""
        self.is_playing = False
    
    def update(self):
        """Update animation playback"""
        if self.is_playing and len(self.frames) > 0:
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_duration:
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.last_update = now
    
    def get_current_frame(self):
        """Get current frame"""
        if 0 <= self.current_frame < len(self.frames):
            return self.frames[self.current_frame]
        return None
    
    def get_frames(self):
        """Get all frames"""
        return self.frames
    
    def clear(self):
        """Clear all frames"""
        self.frames.clear()
        self.current_frame = 0

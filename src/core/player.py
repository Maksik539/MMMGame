"""
Player Class
"""
import pygame
from config import *
from src.graphics.animation import Animation, AnimationManager
from src.graphics.procedural_sprites import ProceduralSpriteGenerator


class Player(pygame.sprite.Sprite):
    """Player character class"""
    
    def __init__(self, x, y):
        """Initialize player"""
        super().__init__()
        
        # Position and movement
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        
        # Stats
        self.hp = PLAYER_HP
        self.speed = PLAYER_SPEED
        
        # Graphics
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        sprite_gen = ProceduralSpriteGenerator()
        self.image = sprite_gen.generate_player_sprite(self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Animation
        self.animation_manager = AnimationManager()
        self._setup_animations()
        
        # State
        self.facing_right = True
        self.on_ground = False
    
    def _setup_animations(self):
        """Setup player animations"""
        sprite_gen = ProceduralSpriteGenerator()
        
        # Idle animation
        idle_frames = [sprite_gen.generate_player_sprite(self.width, self.height, BLUE)]
        self.animation_manager.add_animation("idle", Animation(idle_frames))
        
        # Walk animation
        walk_frames = [
            sprite_gen.generate_player_sprite(self.width, self.height, BLUE),
            sprite_gen.generate_player_sprite(self.width, self.height, (100, 100, 255))
        ]
        self.animation_manager.add_animation("walk", Animation(walk_frames, 200))
    
    def update(self, keys, tiles):
        """Update player state"""
        # Handle input
        self.vx = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vx = -self.speed
            self.facing_right = False
            self.animation_manager.set_animation("walk")
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vx = self.speed
            self.facing_right = True
            self.animation_manager.set_animation("walk")
        else:
            self.animation_manager.set_animation("idle")
        
        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.on_ground:
            self.vy = JUMP_STRENGTH
        
        # Apply gravity
        self.vy += GRAVITY
        
        # Update position
        self.x += self.vx
        self.y += self.vy
        
        # Collision detection (simplified)
        self.on_ground = False
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        
        # Update animation
        self.animation_manager.update()
        frame = self.animation_manager.get_current_frame()
        if frame:
            self.image = frame
    
    def draw(self, surface, camera_x=0, camera_y=0):
        """Draw player"""
        surface.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

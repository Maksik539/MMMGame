"""
Procedural sprite generation for Mage Quest
Creates simple 16x16 pixel art sprites programmatically
"""
import pygame
import random


class ProceduralSpriteGenerator:
    """Generates simple sprites procedurally"""
    
    def __init__(self, sprite_size=16):
        self.sprite_size = sprite_size
        
    def generate_mage_sprite(self, color=(100, 100, 255)):
        """Generate a simple mage sprite"""
        sprite = pygame.Surface((self.sprite_size, self.sprite_size), pygame.SRCALPHA)
        
        # Simple robe shape
        pygame.draw.circle(sprite, color, (8, 10), 6)  # Body
        pygame.draw.circle(sprite, (255, 220, 177), (8, 5), 3)  # Head
        
        # Hat
        hat_color = (50, 50, 150)
        pygame.draw.polygon(sprite, hat_color, [(4, 5), (12, 5), (8, 1)])
        
        return sprite
        
    def generate_skeleton_sprite(self):
        """Generate a skeleton enemy sprite"""
        sprite = pygame.Surface((self.sprite_size, self.sprite_size), pygame.SRCALPHA)
        
        # Bones
        bone_color = (230, 230, 230)
        pygame.draw.circle(sprite, bone_color, (8, 5), 3)  # Skull
        pygame.draw.rect(sprite, bone_color, (7, 8, 2, 6))  # Spine
        
        return sprite
        
    def generate_fire_sphere_sprite(self):
        """Generate a fire sphere enemy sprite"""
        sprite = pygame.Surface((self.sprite_size, self.sprite_size), pygame.SRCALPHA)
        
        # Layered fire effect
        pygame.draw.circle(sprite, (255, 100, 0), (8, 8), 6)  # Outer
        pygame.draw.circle(sprite, (255, 200, 0), (8, 8), 4)  # Middle
        pygame.draw.circle(sprite, (255, 255, 100), (8, 8), 2)  # Core
        
        return sprite
        
    def generate_tornado_sprite(self):
        """Generate a tornado enemy sprite"""
        sprite = pygame.Surface((self.sprite_size, self.sprite_size), pygame.SRCALPHA)
        
        # Spiral pattern
        color = (200, 200, 255, 180)
        for i in range(0, self.sprite_size, 2):
            width = max(1, (self.sprite_size - i) // 4)
            pygame.draw.circle(sprite, color, (8, i), width)
            
        return sprite
        
    def generate_tile_sprite(self, tile_type="floor"):
        """Generate a tile sprite"""
        sprite = pygame.Surface((self.sprite_size, self.sprite_size))
        
        if tile_type == "floor":
            base_color = (80, 80, 80)
            sprite.fill(base_color)
            # Add some texture
            for _ in range(5):
                x = random.randint(0, self.sprite_size - 1)
                y = random.randint(0, self.sprite_size - 1)
                variation = random.randint(-10, 10)
                color = tuple(max(0, min(255, c + variation)) for c in base_color)
                sprite.set_at((x, y), color)
                
        elif tile_type == "wall":
            base_color = (100, 100, 100)
            sprite.fill(base_color)
            # Border
            pygame.draw.rect(sprite, (80, 80, 80), (0, 0, self.sprite_size, self.sprite_size), 1)
            
        elif tile_type == "door":
            sprite.fill((139, 69, 19))  # Wood color
            pygame.draw.rect(sprite, (80, 40, 10), (0, 0, self.sprite_size, self.sprite_size), 2)
            
        return sprite
        
    def generate_projectile_sprite(self, color=(255, 255, 0)):
        """Generate a projectile sprite"""
        sprite = pygame.Surface((8, 8), pygame.SRCALPHA)
        pygame.draw.circle(sprite, color, (4, 4), 3)
        pygame.draw.circle(sprite, (255, 255, 255), (4, 4), 1)  # Glow
        return sprite

"""
Projectile Class
"""
import pygame
from config import *


class Projectile(pygame.sprite.Sprite):
    """Projectile class for bullets and other projectiles"""
    
    def __init__(self, x, y, vx, vy, damage=10, color=WHITE):
        """Initialize projectile"""
        super().__init__()
        
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.damage = damage
        
        # Graphics
        self.image = pygame.Surface((8, 8), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (4, 4), 4)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.lifetime = 180  # 3 seconds at 60 FPS
    
    def update(self):
        """Update projectile"""
        self.x += self.vx
        self.y += self.vy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()
    
    def draw(self, surface, camera_x=0, camera_y=0):
        """Draw projectile"""
        surface.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

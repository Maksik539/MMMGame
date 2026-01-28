"""
Base projectile class for Mage Quest
"""
import pygame
import config


class Projectile(pygame.sprite.Sprite):
    """Base class for all projectiles in the game"""
    
    def __init__(self, x, y, direction, speed, damage, color=(255, 255, 0)):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = speed
        self.damage = damage
        self.lifetime = 300  # frames
        
    def update(self):
        """Update projectile position"""
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed
        self.lifetime -= 1
        
        # Remove if out of bounds or lifetime expired
        if (self.rect.right < 0 or self.rect.left > config.SCREEN_WIDTH or
            self.rect.bottom < 0 or self.rect.top > config.SCREEN_HEIGHT or
            self.lifetime <= 0):
            self.kill()


class PlayerProjectile(Projectile):
    """Projectile fired by the player"""
    
    def __init__(self, x, y, direction):
        super().__init__(
            x, y, direction,
            config.PLAYER_PROJECTILE_SPEED,
            config.PLAYER_PROJECTILE_DAMAGE,
            config.YELLOW
        )


class EnemyProjectile(Projectile):
    """Projectile fired by enemies"""
    
    def __init__(self, x, y, direction, speed=5, damage=5):
        super().__init__(x, y, direction, speed, damage, config.RED)

"""
Player class and related functionality for Mage Quest
"""
import pygame
import math
import config
from src.core.projectiles import PlayerProjectile


class Player(pygame.sprite.Sprite):
    """Main player character"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(config.BLUE)
        self.rect = self.image.get_rect(center=(x, y))
        
        self.health = config.PLAYER_MAX_HEALTH
        self.speed = config.PLAYER_SPEED
        self.projectiles = pygame.sprite.Group()
        self.shoot_cooldown = 0
        self.shoot_delay = 10  # frames between shots
        
    def update(self, keys, mouse_pos):
        """Update player state"""
        # Movement
        dx = 0
        dy = 0
        
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = 1
            
        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            dx *= 0.707
            dy *= 0.707
            
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        
        # Keep player on screen
        self.rect.clamp_ip(pygame.Rect(0, 0, config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        
        # Update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
            
        # Update projectiles
        self.projectiles.update()
        
    def shoot(self, target_pos):
        """Shoot a projectile towards target position"""
        if self.shoot_cooldown <= 0:
            # Calculate direction
            dx = target_pos[0] - self.rect.centerx
            dy = target_pos[1] - self.rect.centery
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance > 0:
                direction = (dx / distance, dy / distance)
                projectile = PlayerProjectile(
                    self.rect.centerx,
                    self.rect.centery,
                    direction
                )
                self.projectiles.add(projectile)
                self.shoot_cooldown = self.shoot_delay
                
    def take_damage(self, amount):
        """Reduce player health"""
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            
    def is_alive(self):
        """Check if player is still alive"""
        return self.health > 0
        
    def draw(self, surface):
        """Draw player and projectiles"""
        surface.blit(self.image, self.rect)
        self.projectiles.draw(surface)

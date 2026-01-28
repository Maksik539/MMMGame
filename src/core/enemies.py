"""
Enemy Classes and Manager
"""
import pygame
import random
from config import *
from src.core.projectiles import Projectile
from src.graphics.asset_coordinator import asset_coordinator


class Enemy(pygame.sprite.Sprite):
    """Base enemy class"""
    
    def __init__(self, x, y, enemy_type="basic"):
        """Initialize enemy"""
        super().__init__()
        
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.enemy_type = enemy_type
        
        # Stats
        self.hp = 50
        self.speed = 2
        self.damage = 10
        
        # Graphics
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # AI
        self.direction = random.choice([-1, 1])
        self.shoot_cooldown = 0
    
    def update(self, player_pos, projectiles):
        """Update enemy"""
        # Simple AI - move towards player
        dx = player_pos[0] - self.x
        
        if abs(dx) > 5:
            self.vx = self.speed if dx > 0 else -self.speed
        else:
            self.vx = 0
        
        # Apply gravity
        self.vy += GRAVITY
        
        # Update position
        self.x += self.vx
        self.y += self.vy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        
        # Shooting
        self.shoot_cooldown -= 1
        if self.shoot_cooldown <= 0 and abs(dx) < 300:
            self._shoot(player_pos, projectiles)
            self.shoot_cooldown = 60  # 1 second at 60 FPS
    
    def _shoot(self, player_pos, projectiles):
        """Shoot projectile towards player"""
        dx = player_pos[0] - self.x
        dy = player_pos[1] - self.y
        distance = max(1, (dx**2 + dy**2) ** 0.5)
        
        # Normalize and scale
        vx = (dx / distance) * 5
        vy = (dy / distance) * 5
        
        projectile = Projectile(self.x, self.y, vx, vy, self.damage, RED)
        projectiles.add(projectile)
    
    def take_damage(self, damage):
        """Take damage"""
        self.hp -= damage
        if self.hp <= 0:
            self.kill()
    
    def draw(self, surface, camera_x=0, camera_y=0):
        """Draw enemy"""
        surface.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))


class EnemyManager:
    """Manages all enemies in the game"""
    
    def __init__(self):
        """Initialize enemy manager"""
        self.enemies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
    
    def add_enemy(self, enemy):
        """Add enemy to manager"""
        self.enemies.add(enemy)
    
    def spawn_enemy(self, x, y, enemy_type="basic"):
        """Spawn new enemy"""
        enemy = Enemy(x, y, enemy_type)
        self.add_enemy(enemy)
        return enemy
    
    def update(self, player_pos):
        """Update all enemies"""
        for enemy in self.enemies:
            enemy.update(player_pos, self.projectiles)
        
        self.projectiles.update()
    
    def draw(self, surface, camera_x=0, camera_y=0):
        """Draw all enemies and projectiles"""
        for enemy in self.enemies:
            enemy.draw(surface, camera_x, camera_y)
        
        for projectile in self.projectiles:
            projectile.draw(surface, camera_x, camera_y)
    
    def clear(self):
        """Clear all enemies and projectiles"""
        self.enemies.empty()
        self.projectiles.empty()

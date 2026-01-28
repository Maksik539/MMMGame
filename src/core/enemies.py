"""
Enemy classes and manager for Mage Quest
"""
import pygame
import random
import math
import config
from src.core.projectiles import EnemyProjectile


class Enemy(pygame.sprite.Sprite):
    """Base enemy class"""
    
    def __init__(self, x, y, color, speed, health):
        super().__init__()
        self.image = pygame.Surface((24, 24))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.health = health
        self.max_health = health
        
    def update(self, player_pos):
        """Update enemy state - to be overridden"""
        pass
        
    def take_damage(self, amount):
        """Reduce enemy health"""
        self.health -= amount
        if self.health <= 0:
            self.kill()
            return True
        return False


class Skeleton(Enemy):
    """Basic melee enemy that chases the player"""
    
    def __init__(self, x, y):
        super().__init__(x, y, config.GRAY, config.SKELETON_SPEED, config.SKELETON_HEALTH)
        
    def update(self, player_pos):
        """Chase the player"""
        dx = player_pos[0] - self.rect.centerx
        dy = player_pos[1] - self.rect.centery
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance > 0:
            dx = (dx / distance) * self.speed
            dy = (dy / distance) * self.speed
            self.rect.x += dx
            self.rect.y += dy


class FireSphere(Enemy):
    """Ranged enemy that shoots fire projectiles"""
    
    def __init__(self, x, y):
        super().__init__(x, y, config.RED, config.FIRE_SPHERE_SPEED, config.FIRE_SPHERE_HEALTH)
        self.shoot_cooldown = 0
        self.shoot_delay = 60
        self.projectiles = pygame.sprite.Group()
        
    def update(self, player_pos):
        """Keep distance and shoot at player"""
        dx = player_pos[0] - self.rect.centerx
        dy = player_pos[1] - self.rect.centery
        distance = math.sqrt(dx**2 + dy**2)
        
        # Keep at medium distance
        if distance < 200:
            # Move away
            if distance > 0:
                dx = -(dx / distance) * self.speed
                dy = -(dy / distance) * self.speed
                self.rect.x += dx
                self.rect.y += dy
        elif distance > 300:
            # Move closer
            if distance > 0:
                dx = (dx / distance) * self.speed
                dy = (dy / distance) * self.speed
                self.rect.x += dx
                self.rect.y += dy
                
        # Shoot at player
        if self.shoot_cooldown <= 0 and distance > 0:
            direction = (dx / distance, dy / distance)
            projectile = EnemyProjectile(
                self.rect.centerx,
                self.rect.centery,
                direction,
                speed=4,
                damage=10
            )
            self.projectiles.add(projectile)
            self.shoot_cooldown = self.shoot_delay
        
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
            
        self.projectiles.update()


class Tornado(Enemy):
    """Fast moving enemy with erratic movement"""
    
    def __init__(self, x, y):
        super().__init__(x, y, config.WHITE, config.TORNADO_SPEED, config.TORNADO_HEALTH)
        self.direction = random.uniform(0, 2 * math.pi)
        self.change_timer = 0
        
    def update(self, player_pos):
        """Move in spiraling pattern towards player"""
        # Change direction periodically
        self.change_timer += 1
        if self.change_timer > 30:
            dx = player_pos[0] - self.rect.centerx
            dy = player_pos[1] - self.rect.centery
            self.direction = math.atan2(dy, dx) + random.uniform(-0.5, 0.5)
            self.change_timer = 0
            
        # Move in current direction
        self.rect.x += math.cos(self.direction) * self.speed
        self.rect.y += math.sin(self.direction) * self.speed


class EnemyManager:
    """Manages enemy spawning and updates"""
    
    def __init__(self):
        self.enemies = pygame.sprite.Group()
        self.spawn_timer = 0
        self.enemy_types = [Skeleton, FireSphere, Tornado]
        
    def update(self, player_pos):
        """Update all enemies and spawn new ones"""
        # Spawn new enemies
        if len(self.enemies) < config.MAX_ENEMIES:
            self.spawn_timer += 1
            if self.spawn_timer >= config.ENEMY_SPAWN_RATE:
                self.spawn_enemy()
                self.spawn_timer = 0
                
        # Update existing enemies
        for enemy in self.enemies:
            enemy.update(player_pos)
            
    def spawn_enemy(self):
        """Spawn a random enemy at screen edge"""
        enemy_type = random.choice(self.enemy_types)
        
        # Random position at screen edge
        side = random.randint(0, 3)
        if side == 0:  # Top
            x = random.randint(0, config.SCREEN_WIDTH)
            y = -20
        elif side == 1:  # Right
            x = config.SCREEN_WIDTH + 20
            y = random.randint(0, config.SCREEN_HEIGHT)
        elif side == 2:  # Bottom
            x = random.randint(0, config.SCREEN_WIDTH)
            y = config.SCREEN_HEIGHT + 20
        else:  # Left
            x = -20
            y = random.randint(0, config.SCREEN_HEIGHT)
            
        enemy = enemy_type(x, y)
        self.enemies.add(enemy)
        
    def draw(self, surface):
        """Draw all enemies"""
        self.enemies.draw(surface)
        
        # Draw projectiles from enemies
        for enemy in self.enemies:
            if hasattr(enemy, 'projectiles'):
                enemy.projectiles.draw(surface)
                
    def get_all_projectiles(self):
        """Get all enemy projectiles"""
        all_projectiles = pygame.sprite.Group()
        for enemy in self.enemies:
            if hasattr(enemy, 'projectiles'):
                all_projectiles.add(enemy.projectiles)
        return all_projectiles

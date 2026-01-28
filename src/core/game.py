"""
Main game loop and logic for Mage Quest
"""
import pygame
import config
from src.core.player import Player
from src.core.enemies import EnemyManager


class Game:
    """Main game class"""
    
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = False
        
        # Initialize game objects
        self.player = Player(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2)
        self.enemy_manager = EnemyManager()
        
        # Fonts
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
    def run(self):
        """Main game loop"""
        self.running = True
        
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(config.FPS)
            
    def handle_events(self):
        """Handle game events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self.player.shoot(pygame.mouse.get_pos())
                    
    def update(self):
        """Update game state"""
        if not self.player.is_alive():
            self.running = False
            return
            
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        
        # Update player
        self.player.update(keys, mouse_pos)
        
        # Update enemies
        self.enemy_manager.update(self.player.rect.center)
        
        # Check collisions
        self.check_collisions()
        
    def check_collisions(self):
        """Check for collisions between game objects"""
        # Player projectiles hitting enemies
        for projectile in self.player.projectiles:
            hit_enemies = pygame.sprite.spritecollide(
                projectile, self.enemy_manager.enemies, False
            )
            if hit_enemies:
                projectile.kill()
                for enemy in hit_enemies:
                    enemy.take_damage(projectile.damage)
                    
        # Enemy projectiles hitting player
        enemy_projectiles = self.enemy_manager.get_all_projectiles()
        hit_projectiles = pygame.sprite.spritecollide(
            self.player, enemy_projectiles, True
        )
        for projectile in hit_projectiles:
            self.player.take_damage(projectile.damage)
            
        # Enemies hitting player
        hit_enemies = pygame.sprite.spritecollide(
            self.player, self.enemy_manager.enemies, False
        )
        for enemy in hit_enemies:
            self.player.take_damage(1)  # Contact damage
            
    def draw(self):
        """Draw game state"""
        self.screen.fill(config.BLACK)
        
        # Draw game objects
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        
        # Draw UI
        self.draw_ui()
        
        pygame.display.flip()
        
    def draw_ui(self):
        """Draw user interface elements"""
        # Health bar
        health_text = self.small_font.render(
            f"Health: {self.player.health}/{config.PLAYER_MAX_HEALTH}",
            True, config.WHITE
        )
        self.screen.blit(health_text, (10, 10))
        
        # Health bar background
        bar_width = 200
        bar_height = 20
        pygame.draw.rect(
            self.screen, config.DARK_GRAY,
            (10, 40, bar_width, bar_height)
        )
        
        # Health bar fill
        health_percent = self.player.health / config.PLAYER_MAX_HEALTH
        fill_width = int(bar_width * health_percent)
        color = config.GREEN if health_percent > 0.5 else config.RED
        pygame.draw.rect(
            self.screen, color,
            (10, 40, fill_width, bar_height)
        )
        
        # Enemy count
        enemy_text = self.small_font.render(
            f"Enemies: {len(self.enemy_manager.enemies)}",
            True, config.WHITE
        )
        self.screen.blit(enemy_text, (10, 70))

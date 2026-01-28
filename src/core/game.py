"""
Main Game Class
"""
import pygame
from config import *
from src.core.player import Player
from src.core.enemies import EnemyManager
from src.world.tilemap import LevelBuilder


class Game:
    """Main game class"""
    
    def __init__(self):
        """Initialize game"""
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("MMMGame")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Game objects
        self.player = Player(100, 100)
        self.enemy_manager = EnemyManager()
        self.level_builder = LevelBuilder()
        
        # Camera
        self.camera_x = 0
        self.camera_y = 0
        
        # Load level
        self._load_test_level()
    
    def _load_test_level(self):
        """Load test level"""
        # Create simple platform
        self.level_builder.add_tile(0, SCREEN_HEIGHT - TILE_SIZE, "ground")
        self.level_builder.add_tile(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE, "ground")
        self.level_builder.add_tile(TILE_SIZE * 2, SCREEN_HEIGHT - TILE_SIZE, "ground")
        self.level_builder.add_tile(TILE_SIZE * 3, SCREEN_HEIGHT - TILE_SIZE, "ground")
        
        # Spawn test enemy
        self.enemy_manager.spawn_enemy(400, 300)
    
    def handle_events(self):
        """Handle game events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def update(self):
        """Update game state"""
        keys = pygame.key.get_pressed()
        
        # Update player
        tiles = self.level_builder.get_tiles()
        self.player.update(keys, tiles)
        
        # Update enemies
        player_pos = (self.player.x, self.player.y)
        self.enemy_manager.update(player_pos)
        
        # Update camera
        self.camera_x = max(0, self.player.x - SCREEN_WIDTH // 2)
        self.camera_y = max(0, self.player.y - SCREEN_HEIGHT // 2)
    
    def draw(self):
        """Draw game"""
        self.screen.fill(BLACK)
        
        # Draw level
        self.level_builder.draw(self.screen, self.camera_x, self.camera_y)
        
        # Draw enemies
        self.enemy_manager.draw(self.screen, self.camera_x, self.camera_y)
        
        # Draw player
        self.player.draw(self.screen, self.camera_x, self.camera_y)
        
        # Draw UI
        self._draw_ui()
        
        pygame.display.flip()
    
    def _draw_ui(self):
        """Draw UI elements"""
        font = pygame.font.Font(None, 36)
        hp_text = font.render(f"HP: {self.player.hp}", True, WHITE)
        self.screen.blit(hp_text, (10, 10))
    
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

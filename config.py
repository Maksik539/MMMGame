"""
Game configuration settings for Mage Quest
"""
import os

# Screen settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
TITLE = "Mage Quest"

# Player settings
PLAYER_SPEED = 5
PLAYER_MAX_HEALTH = 100
PLAYER_PROJECTILE_SPEED = 10
PLAYER_PROJECTILE_DAMAGE = 10

# Enemy settings
SKELETON_SPEED = 2
SKELETON_HEALTH = 30
FIRE_SPHERE_SPEED = 3
FIRE_SPHERE_HEALTH = 20
TORNADO_SPEED = 4
TORNADO_HEALTH = 40

# Tile settings
TILE_SIZE = 16

# Asset paths - relative to project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
SPRITES_DIR = os.path.join(ASSETS_DIR, "sprites")
TILESETS_DIR = os.path.join(ASSETS_DIR, "tilesets")
LEVELS_DIR = os.path.join(BASE_DIR, "levels")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

# Game settings
MAX_ENEMIES = 20
ENEMY_SPAWN_RATE = 60  # frames between spawns

"""
Procedural Sprite Generator
"""
import pygame
from config import *


class ProceduralSpriteGenerator:
    """Generates sprites procedurally"""
    
    @staticmethod
    def generate_player_sprite(width=32, height=32, color=BLUE):
        """Generate basic player sprite"""
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(surface, color, (0, 0, width, height))
        pygame.draw.circle(surface, WHITE, (width // 2, height // 3), 5)
        return surface
    
    @staticmethod
    def generate_enemy_sprite(width=32, height=32, color=RED):
        """Generate basic enemy sprite"""
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(surface, color, (0, 0, width, height))
        pygame.draw.circle(surface, WHITE, (width // 3, height // 3), 3)
        pygame.draw.circle(surface, WHITE, (2 * width // 3, height // 3), 3)
        return surface
    
    @staticmethod
    def generate_tile_sprite(width=32, height=32, color=GRAY):
        """Generate basic tile sprite"""
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(surface, color, (0, 0, width, height))
        pygame.draw.rect(surface, BLACK, (0, 0, width, height), 1)
        return surface
    
    @staticmethod
    def generate_projectile_sprite(width=8, height=8, color=WHITE):
        """Generate projectile sprite"""
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.circle(surface, color, (width // 2, height // 2), min(width, height) // 2)
        return surface

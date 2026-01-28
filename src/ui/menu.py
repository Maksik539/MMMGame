"""
Main Menu
"""
import pygame
from config import *


class Menu:
    """Main menu class"""
    
    def __init__(self):
        """Initialize menu"""
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("MMMGame - Menu")
        self.clock = pygame.time.Clock()
        
        # Menu options
        self.options = ["Start Game", "Level Editor", "Quit"]
        self.selected = 0
        
        # Font
        self.font_large = pygame.font.Font(None, 72)
        self.font_medium = pygame.font.Font(None, 48)
    
    def handle_events(self):
        """Handle menu events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected = (self.selected - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected = (self.selected + 1) % len(self.options)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    if self.selected == 0:
                        return "start"
                    elif self.selected == 1:
                        return "editor"
                    elif self.selected == 2:
                        return "quit"
                elif event.key == pygame.K_ESCAPE:
                    return "quit"
        return None
    
    def draw(self):
        """Draw menu"""
        self.screen.fill(BLACK)
        
        # Draw title
        title = self.font_large.render("MMMGame", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
        self.screen.blit(title, title_rect)
        
        # Draw options
        for i, option in enumerate(self.options):
            color = GREEN if i == self.selected else WHITE
            text = self.font_medium.render(option, True, color)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 300 + i * 70))
            self.screen.blit(text, text_rect)
        
        pygame.display.flip()
    
    def run(self):
        """Run menu loop"""
        running = True
        choice = None
        
        while running:
            result = self.handle_events()
            if result:
                choice = result
                running = False
            
            self.draw()
            self.clock.tick(FPS)
        
        return choice

"""
Mage Quest - Main entry point
A procedurally generated dungeon crawler game
"""
import sys
import pygame

from src.ui.menu import MainMenu
from src.core.game import Game
import config


def main():
    """Main game loop"""
    pygame.init()
    
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    clock = pygame.time.Clock()
    
    # Show main menu
    menu = MainMenu(screen)
    running = True
    
    while running:
        choice = menu.run()
        
        if choice == "play":
            # Start the game
            game = Game(screen)
            game.run()
        elif choice == "editor":
            # Launch level editor
            try:
                from src.editor.launcher import launch_editor
                launch_editor()
            except Exception as e:
                print(f"Error launching editor: {e}")
        elif choice == "quit":
            running = False
        
        clock.tick(config.FPS)
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

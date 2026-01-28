"""
MMMGame - Main Entry Point
"""
import pygame
from src.ui.menu import Menu
from src.core.game import Game
from src.graphics.asset_coordinator import asset_coordinator


def main():
    """Main game loop"""
    pygame.init()
    
    # Initialize asset coordinator
    asset_coordinator.initialize()
    
    # Show menu
    menu = Menu()
    choice = menu.run()
    
    if choice == "start":
        # Start game
        game = Game()
        game.run()
    elif choice == "editor":
        # Start level editor
        from src.editor.launcher import launch_editor
        launch_editor()
    
    pygame.quit()


if __name__ == "__main__":
    main()

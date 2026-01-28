"""
Launcher for the level editor
Can be run standalone or called from main game
"""
import sys
import pygame
from src.editor.level_editor import LevelEditor


def launch_editor():
    """Launch the level editor"""
    editor = LevelEditor()
    editor.run()
    pygame.quit()


if __name__ == "__main__":
    launch_editor()
    sys.exit()

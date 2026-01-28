"""
Level Editor Launcher
"""
import pygame
from config import *


def launch_editor():
    """Launch the level editor"""
    from src.editor.level_editor import LevelEditor
    
    editor = LevelEditor()
    editor.run()

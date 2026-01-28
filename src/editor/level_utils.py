"""
Level Editor Utilities
"""
import json
import os
from config import *


class LevelUtils:
    """Utility functions for level editor"""
    
    @staticmethod
    def save_level(level_data, filename):
        """Save level to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(level_data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving level: {e}")
            return False
    
    @staticmethod
    def load_level(filename):
        """Load level from JSON file"""
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    return json.load(f)
            return None
        except Exception as e:
            print(f"Error loading level: {e}")
            return None
    
    @staticmethod
    def validate_level(level_data):
        """Validate level data structure"""
        required_keys = ['rooms', 'connections']
        return all(key in level_data for key in required_keys)
    
    @staticmethod
    def create_new_level():
        """Create new empty level"""
        return {
            'rooms': [],
            'connections': [],
            'metadata': {
                'name': 'New Level',
                'author': '',
                'version': '1.0'
            }
        }

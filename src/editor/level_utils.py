"""
Level utilities for the editor
"""
import json
import os
import config


class LevelUtils:
    """Utility functions for level management"""
    
    @staticmethod
    def save_level(level_data, filename):
        """Save level data to JSON file"""
        filepath = os.path.join(config.LEVELS_DIR, filename)
        with open(filepath, 'w') as f:
            json.dump(level_data, f, indent=2)
            
    @staticmethod
    def load_level(filename):
        """Load level data from JSON file"""
        filepath = os.path.join(config.LEVELS_DIR, filename)
        if not os.path.exists(filepath):
            return None
            
        with open(filepath, 'r') as f:
            return json.load(f)
            
    @staticmethod
    def list_levels():
        """List all available levels"""
        if not os.path.exists(config.LEVELS_DIR):
            os.makedirs(config.LEVELS_DIR)
            return []
            
        levels = []
        for filename in os.listdir(config.LEVELS_DIR):
            if filename.endswith('.json'):
                levels.append(filename)
        return sorted(levels)
        
    @staticmethod
    def create_empty_level(width, height):
        """Create an empty level structure"""
        return {
            "width": width,
            "height": height,
            "tiles": [[0 for _ in range(width)] for _ in range(height)],
            "entities": [],
            "properties": {}
        }
        
    @staticmethod
    def validate_level(level_data):
        """Validate level data structure"""
        required_keys = ["width", "height", "tiles"]
        for key in required_keys:
            if key not in level_data:
                return False
        return True

"""
Undo/Redo System
"""
from config import *


class HistoryManager:
    """Manages undo/redo history"""
    
    def __init__(self, max_history=50):
        """Initialize history manager"""
        self.max_history = max_history
        self.history = []
        self.current_index = -1
    
    def add_action(self, action):
        """Add action to history"""
        # Remove any actions after current index
        self.history = self.history[:self.current_index + 1]
        
        # Add new action
        self.history.append(action)
        
        # Limit history size
        if len(self.history) > self.max_history:
            self.history.pop(0)
        else:
            self.current_index += 1
    
    def undo(self):
        """Undo last action"""
        if self.can_undo():
            action = self.history[self.current_index]
            self.current_index -= 1
            return action
        return None
    
    def redo(self):
        """Redo last undone action"""
        if self.can_redo():
            self.current_index += 1
            action = self.history[self.current_index]
            return action
        return None
    
    def can_undo(self):
        """Check if undo is possible"""
        return self.current_index >= 0
    
    def can_redo(self):
        """Check if redo is possible"""
        return self.current_index < len(self.history) - 1
    
    def clear(self):
        """Clear history"""
        self.history.clear()
        self.current_index = -1

"""
Undo/Redo history manager for the level editor
"""


class HistoryManager:
    """Manages undo/redo history for editor actions"""
    
    def __init__(self, max_history=50):
        self.max_history = max_history
        self.undo_stack = []
        self.redo_stack = []
        
    def add_action(self, action):
        """Add a new action to history"""
        self.undo_stack.append(action)
        if len(self.undo_stack) > self.max_history:
            self.undo_stack.pop(0)
        # Clear redo stack when new action is added
        self.redo_stack.clear()
        
    def undo(self):
        """Undo the last action"""
        if self.undo_stack:
            action = self.undo_stack.pop()
            self.redo_stack.append(action)
            return action
        return None
        
    def redo(self):
        """Redo the last undone action"""
        if self.redo_stack:
            action = self.redo_stack.pop()
            self.undo_stack.append(action)
            return action
        return None
        
    def can_undo(self):
        """Check if undo is available"""
        return len(self.undo_stack) > 0
        
    def can_redo(self):
        """Check if redo is available"""
        return len(self.redo_stack) > 0
        
    def clear(self):
        """Clear all history"""
        self.undo_stack.clear()
        self.redo_stack.clear()

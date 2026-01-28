"""
Room Editor
"""
import pygame
from config import *
from src.editor.texture_loader import texture_loader


class RoomEditor:
    """Editor for individual rooms"""
    
    def __init__(self, width=20, height=15):
        """Initialize room editor"""
        self.width = width
        self.height = height
        self.tiles = {}  # Dictionary of (x, y): tile_data
        self.objects = []
        self.camera_x = 0
        self.camera_y = 0
        self.grid_size = TILE_SIZE
        self.show_grid = True
        
        # Current tool
        self.current_tool = "paint"
        self.current_texture = None
        
        # Room properties
        self.room_name = "Untitled Room"
        self.background_color = BLACK
    
    def set_tile(self, grid_x, grid_y, texture_name):
        """Set tile at grid position"""
        if 0 <= grid_x < self.width and 0 <= grid_y < self.height:
            self.tiles[(grid_x, grid_y)] = {
                'texture': texture_name,
                'properties': {}
            }
    
    def remove_tile(self, grid_x, grid_y):
        """Remove tile at grid position"""
        if (grid_x, grid_y) in self.tiles:
            del self.tiles[(grid_x, grid_y)]
    
    def get_tile(self, grid_x, grid_y):
        """Get tile at grid position"""
        return self.tiles.get((grid_x, grid_y))
    
    def screen_to_grid(self, screen_x, screen_y):
        """Convert screen coordinates to grid coordinates"""
        grid_x = (screen_x + self.camera_x) // self.grid_size
        grid_y = (screen_y + self.camera_y) // self.grid_size
        return grid_x, grid_y
    
    def grid_to_screen(self, grid_x, grid_y):
        """Convert grid coordinates to screen coordinates"""
        screen_x = grid_x * self.grid_size - self.camera_x
        screen_y = grid_y * self.grid_size - self.camera_y
        return screen_x, screen_y
    
    def handle_event(self, event):
        """Handle room editor events"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                grid_x, grid_y = self.screen_to_grid(*event.pos)
                if self.current_tool == "paint" and self.current_texture:
                    self.set_tile(grid_x, grid_y, self.current_texture)
                elif self.current_tool == "erase":
                    self.remove_tile(grid_x, grid_y)
    
    def set_current_texture(self, texture_name):
        """Set current texture for painting"""
        self.current_texture = texture_name
    
    def set_tool(self, tool):
        """Set current editing tool"""
        self.current_tool = tool
    
    def draw(self, surface, view_rect):
        """Draw room editor"""
        # Draw background
        surface.fill(self.background_color)
        
        # Draw grid
        if self.show_grid:
            self._draw_grid(surface, view_rect)
        
        # Draw tiles
        for (grid_x, grid_y), tile_data in self.tiles.items():
            screen_x, screen_y = self.grid_to_screen(grid_x, grid_y)
            
            # Only draw if visible
            if (view_rect.left <= screen_x < view_rect.right and
                view_rect.top <= screen_y < view_rect.bottom):
                
                texture = texture_loader.get_texture(tile_data['texture'])
                if texture:
                    scaled = pygame.transform.scale(texture, (self.grid_size, self.grid_size))
                    surface.blit(scaled, (screen_x, screen_y))
    
    def _draw_grid(self, surface, view_rect):
        """Draw grid lines"""
        grid_color = (60, 60, 60)
        
        # Vertical lines
        start_x = (view_rect.left // self.grid_size) * self.grid_size
        for x in range(start_x, view_rect.right, self.grid_size):
            screen_x = x - self.camera_x
            pygame.draw.line(surface, grid_color, (screen_x, 0), (screen_x, view_rect.height))
        
        # Horizontal lines
        start_y = (view_rect.top // self.grid_size) * self.grid_size
        for y in range(start_y, view_rect.bottom, self.grid_size):
            screen_y = y - self.camera_y
            pygame.draw.line(surface, grid_color, (0, screen_y), (view_rect.width, screen_y))
    
    def export_data(self):
        """Export room data"""
        return {
            'name': self.room_name,
            'width': self.width,
            'height': self.height,
            'tiles': [(x, y, data) for (x, y), data in self.tiles.items()],
            'objects': self.objects,
            'background_color': self.background_color
        }
    
    def import_data(self, data):
        """Import room data"""
        self.room_name = data.get('name', 'Untitled Room')
        self.width = data.get('width', 20)
        self.height = data.get('height', 15)
        self.background_color = data.get('background_color', BLACK)
        
        # Import tiles
        self.tiles.clear()
        for x, y, tile_data in data.get('tiles', []):
            self.tiles[(x, y)] = tile_data
        
        # Import objects
        self.objects = data.get('objects', [])

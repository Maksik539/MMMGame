"""
Texture Panel
"""
import pygame
from config import *
from src.editor.texture_loader import texture_loader
from src.graphics.procedural_sprites import ProceduralSpriteGenerator


class TexturePanel:
    """Panel for selecting textures"""
    
    def __init__(self, x, y, width, height):
        """Initialize texture panel"""
        self.rect = pygame.Rect(x, y, width, height)
        self.selected_texture = None
        self.scroll_offset = 0
        self.tile_size = 48
        
        # Load textures
        texture_loader.scan_assets_directory()
        
        # Generate default textures if none exist
        if not texture_loader.get_all_textures():
            self._generate_default_textures()
    
    def _generate_default_textures(self):
        """Generate default procedural textures"""
        sprite_gen = ProceduralSpriteGenerator()
        
        # Create some default textures
        textures = {
            'ground': sprite_gen.generate_tile_sprite(TILE_SIZE, TILE_SIZE, (100, 100, 100)),
            'wall': sprite_gen.generate_tile_sprite(TILE_SIZE, TILE_SIZE, (80, 80, 80)),
            'grass': sprite_gen.generate_tile_sprite(TILE_SIZE, TILE_SIZE, (50, 150, 50)),
        }
        
        for name, surface in textures.items():
            texture_loader.textures[name] = surface
            texture_loader.texture_names.append(name)
    
    def handle_event(self, event):
        """Handle panel events"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if event.button == 1:  # Left click
                    self._select_texture(event.pos)
                elif event.button == 4:  # Scroll up
                    self.scroll_offset = max(0, self.scroll_offset - 1)
                elif event.button == 5:  # Scroll down
                    textures = texture_loader.get_all_textures()
                    tiles_per_row = max(1, (self.rect.width - 10) // (self.tile_size + 5))
                    max_scroll = max(0, (len(textures) + tiles_per_row - 1) // tiles_per_row - (self.rect.height - 30) // (self.tile_size + 5))
                    self.scroll_offset = min(max_scroll, self.scroll_offset + 1)
    
    def _select_texture(self, pos):
        """Select texture at position"""
        relative_x = pos[0] - self.rect.x
        relative_y = pos[1] - self.rect.y - 30  # Account for title bar
        
        if relative_y < 0:
            return
        
        textures = texture_loader.get_all_textures()
        tiles_per_row = max(1, (self.rect.width - 10) // (self.tile_size + 5))
        
        col = relative_x // (self.tile_size + 5)
        row = (relative_y // (self.tile_size + 5)) + self.scroll_offset
        
        index = row * tiles_per_row + col
        
        if 0 <= index < len(textures):
            self.selected_texture = textures[index]
    
    def get_selected_texture(self):
        """Get currently selected texture"""
        return self.selected_texture
    
    def draw(self, surface):
        """Draw texture panel"""
        # Draw background
        pygame.draw.rect(surface, (40, 40, 40), self.rect)
        
        # Draw title
        font = pygame.font.Font(None, 24)
        title = font.render("Textures", True, WHITE)
        surface.blit(title, (self.rect.x + 5, self.rect.y + 5))
        
        # Draw textures
        textures = texture_loader.get_all_textures()
        tiles_per_row = max(1, (self.rect.width - 10) // (self.tile_size + 5))
        
        x_offset = self.rect.x + 5
        y_offset = self.rect.y + 30
        
        for i, texture_name in enumerate(textures):
            row = i // tiles_per_row - self.scroll_offset
            col = i % tiles_per_row
            
            if row < 0:
                continue
            
            x = x_offset + col * (self.tile_size + 5)
            y = y_offset + row * (self.tile_size + 5)
            
            if y > self.rect.bottom:
                break
            
            texture = texture_loader.get_texture(texture_name)
            if texture:
                # Scale texture to tile size
                scaled = pygame.transform.scale(texture, (self.tile_size, self.tile_size))
                surface.blit(scaled, (x, y))
                
                # Highlight selected
                if texture_name == self.selected_texture:
                    pygame.draw.rect(surface, GREEN, (x, y, self.tile_size, self.tile_size), 2)
        
        # Draw border
        pygame.draw.rect(surface, (80, 80, 80), self.rect, 1)

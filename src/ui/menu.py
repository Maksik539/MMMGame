"""
Main menu and UI components for Mage Quest
"""
import pygame
import config


class Button:
    """Simple button UI element"""
    
    def __init__(self, x, y, width, height, text, color=config.BLUE):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = tuple(min(255, c + 30) for c in color)
        self.is_hovered = False
        self.font = pygame.font.Font(None, 36)
        
    def draw(self, surface):
        """Draw the button"""
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, config.WHITE, self.rect, 2)
        
        text_surface = self.font.render(self.text, True, config.WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def update(self, mouse_pos):
        """Update button state"""
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        
    def is_clicked(self, mouse_pos, mouse_pressed):
        """Check if button is clicked"""
        return self.rect.collidepoint(mouse_pos) and mouse_pressed[0]


class MainMenu:
    """Main menu screen"""
    
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        
        # Create buttons
        button_width = 300
        button_height = 60
        button_x = config.SCREEN_WIDTH // 2 - button_width // 2
        start_y = config.SCREEN_HEIGHT // 2 - 100
        
        self.buttons = {
            "play": Button(button_x, start_y, button_width, button_height, "Play Game"),
            "editor": Button(button_x, start_y + 80, button_width, button_height, "Level Editor"),
            "quit": Button(button_x, start_y + 160, button_width, button_height, "Quit")
        }
        
        self.title_font = pygame.font.Font(None, 72)
        
    def run(self):
        """Run the main menu"""
        running = True
        
        while running:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return "quit"
                        
            # Update buttons
            for button in self.buttons.values():
                button.update(mouse_pos)
                
            # Check for clicks
            for name, button in self.buttons.items():
                if button.is_clicked(mouse_pos, mouse_pressed):
                    return name
                    
            # Draw
            self.screen.fill(config.BLACK)
            
            # Draw title
            title = self.title_font.render("Mage Quest", True, config.YELLOW)
            title_rect = title.get_rect(center=(config.SCREEN_WIDTH // 2, 150))
            self.screen.blit(title, title_rect)
            
            # Draw subtitle
            subtitle_font = pygame.font.Font(None, 24)
            subtitle = subtitle_font.render(
                "A Procedurally Generated Dungeon Crawler",
                True, config.WHITE
            )
            subtitle_rect = subtitle.get_rect(center=(config.SCREEN_WIDTH // 2, 200))
            self.screen.blit(subtitle, subtitle_rect)
            
            # Draw buttons
            for button in self.buttons.values():
                button.draw(self.screen)
                
            pygame.display.flip()
            self.clock.tick(config.FPS)
            
        return "quit"

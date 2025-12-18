import pygame
import sys
import subprocess
from scripts.utils import load_image

class Menu:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        
        pygame.display.set_caption("Ninja Game")
        self.screen = pygame.display.set_mode((640, 480))
        
        self.display = pygame.Surface((320, 240), pygame.SRCALPHA)
        # self.display_2 = pygame.Surface((320, 240))
        
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont('open sans', 50)

        try:
            bg = load_image("background_menu.png")
        except Exception:
            bg = load_image("background/background_menu.png")
        
        self.assets = {
            "background": pygame.transform.scale(bg, self.screen.get_size()),
        }

    def draw(self):
        # self.display.fill((0, 0, 0, 0))
        self.screen.blit(self.assets["background"], (0, 0))
        
        text_title = self.font.render("Ninja Game", True, (255, 50, 50))
        
        text_game = self.font.render("'G' to start the game", True, (255, 255, 255))
        
        text_editor = self.font.render("'E' to start the editor", True, (255, 255, 255))
        
        self.screen.blit(text_title, (130, 20))
        self.screen.blit(text_game, (50, 180))
        self.screen.blit(text_editor, (50, 280))
        
        pygame.display.flip()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    self.start_game()
                if event.key == pygame.K_e:
                    self.start_editor()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                            
    def start_game(self):
        pygame.quit()
        sys.exit(subprocess.run(["python", "main.py"]).returncode)

    def start_editor(self):
        pygame.quit()
        sys.exit(subprocess.run(["python", "editor.py"]).returncode)
    
    def run(self):
        running = True
        while running:
            self.draw()
            self.events()
            pygame.time.delay(100)
            pygame.display.update()
        self.clock.tick(60)

Menu().run()
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

### Function to not get a black screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    clock.tick(60)

    
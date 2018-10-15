import pygame, sys, random
from pygame.locals import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 30

FPSCLOCK = pygame.time.Clock()


def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((800,600))
    
    pygame.display.set_caption("Test")
    
    DISPLAYSURF.fill((255,255,255))
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == "__main__":
    main()
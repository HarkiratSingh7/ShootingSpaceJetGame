import pygame
from src.res import *

class star(pygame.sprite.Sprite):
    def __init__(self, origin):
        super().__init__()
        self.x = origin[0]
        self.y = origin[1]
        self.valid = True
    
    def update(self):
        if self.y < SCREEN_HEIGHT:
            self.y += STAR_DISP
        else:
            self.valid = False

    def draw(self, surface):
        pygame.draw.circle(surface, (255,255,255), (self.x, self.y), 1)
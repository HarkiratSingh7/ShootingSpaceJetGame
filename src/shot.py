import pygame
from src.res import *

class shot(pygame.sprite.Sprite):
    def __init__(self, origin):
        super().__init__()
        self.image = pygame.image.load(SHOT_IMG)
        self.image = pygame.transform.scale(self.image, SHOT_SCALE)
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.center = origin
        self.valid = True

    def update(self):
        if self.rect.top > 0:
            self.rect.move_ip(0, -DY_SHOT)
        else:
            self.valid = False
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def move(self, surface):
        self.update()
        self.draw(surface)
        
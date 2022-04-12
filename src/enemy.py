import pygame
from src.res import *

class enemy(pygame.sprite.Sprite):
    def __init__(self, origin, jdg):
        super().__init__()
        self.image = pygame.image.load(ENEMY_IMG)
        self.image = pygame.transform.scale(self.image, ENEMY_SCALE)
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.center = origin
        self.valid = True
        self.jdg = jdg

    def shotCollided(self, fire, surface):
        if self.rect.left <= fire.rect.left and self.rect.right >= fire.rect.right:
            if self.rect.top <= fire.rect.top and self.rect.bottom >= fire.rect.bottom:
                self.jdg.addPoints()
                return True
        return False

    def update(self):
        if self.rect.top < SCREEN_HEIGHT:
            self.rect.move_ip(0, DY_ENEMY)
        else:
            self.valid = False
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def move(self, surface):
        self.update()
        self.draw(surface)
        
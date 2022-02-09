import pygame
from res import *

class enemy(pygame.sprite.Sprite):
    def __init__(self, origin):
        super().__init__()
        self.image = pygame.image.load(ENEMY_IMG)
        self.image = pygame.transform.scale(self.image, ENEMY_SCALE)
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.center = origin
        self.valid = True

    def shotCollided(self, fire):
        if self.rect.left <= fire.rect.left and self.rect.right >= fire.rect.right:
            if self.rect.top <= fire.rect.top and self.rect.bottom >= fire.rect.bottom:
                return True

    def update(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.move_ip(0, DY_ENEMY)
        else:
            self.valid = False
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def move(self, surface):
        self.update()
        self.draw(surface)
        
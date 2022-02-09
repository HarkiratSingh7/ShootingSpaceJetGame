import pygame
from res import *

class explosion(pygame.sprite.Sprite):
    def __init__(self, origin):
        super().__init__()
        self.image = pygame.image.load(EXPLOSION_IMG)
        self.scale = EXPLOSION_SCALE
        self.image = pygame.transform.scale(self.image, self.scale)
        self.rect = self.image.get_rect()
        self.rect.center = origin
        self.valid = True
        self.ticks = 0
        self.timepoint = pygame.time.get_ticks()
    
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.timepoint > FPS:
            self.image = pygame.transform.scale(self.image, (self.scale[0] * 1.1, self.scale[1] * 1.3))
            self.ticks += 1
        if self.ticks >= EXPLOSION_LAST:
            self.valid = False
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.move_ip(0, DY_ENEMY)
        else:
            self.valid = False
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
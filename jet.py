import pygame
from res import *
from shot import shot
import pygame.locals as pygloc

class jet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(JET_IMG)
        self.image = pygame.transform.scale(self.image, JET_SCALE)
        self.rect = self.image.get_rect()
        self.rect.center = JET_CENTER

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[pygloc.K_LEFT]:
            self.rect.move_ip(-DX_JET, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[pygloc.K_RIGHT]:
            self.rect.move_ip(DX_JET, 0)
        if self.rect.top > 0 and pressed_keys[pygloc.K_UP]:
            self.rect.move_ip(0, -DY_JET)
        if self.rect.bottom < SCREEN_HEIGHT and pressed_keys[pygloc.K_DOWN]:
            self.rect.move_ip(0, DY_JET)
    
    def fireUp(self, Shots):
        fire = shot((self.rect.centerx, self.rect.top))
        Shots.append(fire)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
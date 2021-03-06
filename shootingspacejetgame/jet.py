import pygame
from shootingspacejetgame.res import *
from shootingspacejetgame.shot import shot
import pygame.locals as pygloc

class jet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(JET_IMG)
        self.image = pygame.transform.scale(self.image, JET_SCALE)
        self.rect = self.image.get_rect()
        self.rect.center = JET_CENTER

    def enemyCollided(self, ene):
        if not (self.rect.bottom - ene.rect.top >= ALLOWED_JET_ENEMY_OVERLAP):
            return False
        # Case if enemy collided at right side
        if self.rect.left >= ene.rect.left and self.rect.left <= ene.rect.right:
            if ene.rect.bottom - self.rect.top >= ALLOWED_JET_ENEMY_OVERLAP:
                return True
        # Case if enemy collided at left side
        if self.rect.right > ene.rect.left and self.rect.right <= ene.rect.right:
            if ene.rect.bottom - self.rect.top >= ALLOWED_JET_ENEMY_OVERLAP:
                return True
        return False

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[pygloc.K_LEFT]:
            self.rect.move_ip(-DX_JET, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[pygloc.K_RIGHT]:
            self.rect.move_ip(DX_JET, 0)
        # if self.rect.top > 0 and pressed_keys[pygloc.K_UP]:
        #     self.rect.move_ip(0, -DY_JET)
        # if self.rect.bottom < SCREEN_HEIGHT and pressed_keys[pygloc.K_DOWN]:
        #     self.rect.move_ip(0, DY_JET)
    
    def fireUp(self, Shots):
        fire = shot((self.rect.centerx, self.rect.top))
        Shots.append(fire)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
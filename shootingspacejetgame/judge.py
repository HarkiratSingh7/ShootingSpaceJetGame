from ctypes.wintypes import POINT
import pygame
from shootingspacejetgame.res import *

class judge:
    def __init__(self, surface):
        self.valid = True 
        self.points = 0
        self.surface = surface
        self.fontname = pygame.font.get_default_font()
        self.font = pygame.font.Font(self.fontname, FONT_SIZE)
        
    def addPoints(self):
        self.points += POINTS_FOR_HITTING_ENEMY

    def display(self):
        text = self.font.render('Score: {0}'.format(self.points), True, LIGHT, DARK)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH - textRect.width // 2 - SCORE_PADDING, textRect.height // 2 + SCORE_PADDING)
        self.surface.blit(text, textRect)

    def endGame(self):
        self.valid = False
        pos = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        
        text1 = self.font.render('Game Ended!', True, LIGHT, DARK)
        textRect1 = text1.get_rect()

        text2 = self.font.render('Your Score: {0}'.format(self.points), True, LIGHT, DARK)
        textRect2 = text2.get_rect()

        text3 = self.font.render('Press S to start again.', True, LIGHT, DARK)
        textRect3 = text3.get_rect()

        textRect1.center = (pos[0], pos[1] - FONT_SIZE - SCORE_PADDING)
        textRect2.center = pos
        textRect3.center = (pos[0], pos[1] + FONT_SIZE + SCORE_PADDING)

        self.surface.blit(text1, textRect1)
        self.surface.blit(text2, textRect2)
        self.surface.blit(text3, textRect3)

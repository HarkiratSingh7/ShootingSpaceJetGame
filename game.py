import pygame, sys, random
from jet import jet
from enemy import enemy
import pygame.locals as pygloc
from res import *

pygame.init()
FramePerSec = pygame.time.Clock()

GameScreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GameScreen.fill(DARK)

pygame.display.set_caption(TITLE)

# Participants
Player = jet()
Shots = []
Enemies = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Player.fireUp(Shots)

    # Generate enemies
    if len(Enemies) <= 5:
        pos = (random.randint(ENEMY_SCALE[0] // 2, SCREEN_WIDTH - ENEMY_SCALE[0] // 2), 0)
        new_enemy = enemy(pos)
        Enemies.append(new_enemy)
    # Events
    Player.update()
    for fire in Shots:
        fire.update()
    Shots = list(filter(lambda fire: fire.valid, Shots))

    for ene in Enemies:
        ene.update()
        index = ene.rect.collidelist(Shots)
        if index >= 0:
            Enemies.remove(ene)
            Shots.pop(index)
    Enemies = list(filter(lambda ene: ene.valid, Enemies))    

    if Player.rect.collidelist(Enemies) >= 0:
        # Game Over
        raise 'Game Over'

    # Updates
    GameScreen.fill(DARK)
    Player.draw(GameScreen)
    for fire in Shots:
        fire.draw(GameScreen)
    for ene in Enemies:
        ene.draw(GameScreen)
    pygame.display.update()
    FramePerSec.tick(FPS)
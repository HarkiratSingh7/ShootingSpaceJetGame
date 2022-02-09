import pygame, sys, random
from jet import jet
from enemy import enemy
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
    # Game Global Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Player.fireUp(Shots)

    # Generate non overlapping enemies
    if len(Enemies) < MIN_ENSURE_ENEMIES:
        count = random.randint(MIN_GEN_ENEMIES, MAX_GEN_ENEMIES)
        for i in range(count):
            pos = (random.randint(ENEMY_SCALE[0] // 2, SCREEN_WIDTH - ENEMY_SCALE[0] // 2), 0)
            new_enemy = enemy(pos)
            if new_enemy.rect.collidelist(Enemies) < 0:
                Enemies.append(new_enemy)
    
    # Updates
    Player.update()
    for fire in Shots:
        fire.update()
    
    # Check if shots went out of view
    Shots = list(filter(lambda fire: fire.valid, Shots))

    # Check if enemies were hit by shots
    for ene in Enemies:
        ene.update()
        for fire in Shots:
            if ene.shotCollided(fire):
                Enemies.remove(ene)
                Shots.remove(fire)

    # Check if the enemies went out of view            
    Enemies = list(filter(lambda ene: ene.valid, Enemies))    

    # Check if the player jet collided with enemy
    for ene in Enemies:
        if Player.enemyCollided(ene):
            raise 'Game Over'

    # Update the screen
    GameScreen.fill(DARK)       # Clear Screen
    Player.draw(GameScreen)     # Player Jet
    for fire in Shots:
        fire.draw(GameScreen)   # Shots
    for ene in Enemies:
        ene.draw(GameScreen)    # Enemies
    pygame.display.update()     # Update the screen
    
    FramePerSec.tick(FPS)       
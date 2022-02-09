import pygame, sys, random
from explosion import explosion
from jet import jet
from enemy import enemy
from judge import judge
from star import star
from res import *

pygame.init()
FramePerSec = pygame.time.Clock()

GameScreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GameScreen.fill(DARK)

pygame.display.set_caption(TITLE)

ShowWelcome = True

def Welcome(surface):
    pos = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    fontname = pygame.font.get_default_font()
    font = pygame.font.Font(fontname, FONT_SIZE)
    text = font.render('Press S to start game.', True, LIGHT, DARK)
    textRect = text.get_rect()
    textRect.center = (pos[0], pos[1] - FONT_SIZE)
    text1 = font.render('Press Space to shoot in game.', True, LIGHT, DARK)
    textRect1 = text1.get_rect()
    textRect1.center = pos
    text2 = font.render('Use left, right keys for navigation.', True, LIGHT, DARK)
    textRect2 = text2.get_rect()
    textRect2.center = (pos[0], pos[1] + FONT_SIZE)
    surface.blit(text, textRect)
    surface.blit(text1, textRect1)
    surface.blit(text2, textRect2)

# Participants
Player = jet()
Shots = []
Explosions = []
Enemies = []
Stars = [
        star((random.randint(0, SCREEN_WIDTH),random.randint(0, SCREEN_HEIGHT)))
		for _ in range(STARS_N)
	]
Judge = judge(GameScreen)

while True:
    if ShowWelcome:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    Player = jet()
                    Shots = []
                    ShowWelcome = False
                    Enemies = []
                    Explosions = []
                    Judge = judge(GameScreen)
        
        pygame.display.update()
        FramePerSec.tick(FPS)
        GameScreen.fill(DARK)
        Welcome(GameScreen)
        continue

    if not Judge.valid:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    Player = jet()
                    Shots = []
                    Enemies = []
                    Explosions = []
                    Judge = judge(GameScreen)

        if not Judge.valid:
            GameScreen.fill(DARK)
            Judge.endGame()
            pygame.display.update()
            FramePerSec.tick(FPS)

    while Judge.valid:
        # Game Global Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Player.fireUp(Shots)

        # Generate Stars
        for _ in range(STAR_DISP):
            st = star((random.randint(0, SCREEN_WIDTH),random.randint(0, 0)))
            Stars.append(st)

        # Generate non overlapping enemies
        if len(Enemies) < MIN_ENSURE_ENEMIES:
            count = random.randint(MIN_GEN_ENEMIES, MAX_GEN_ENEMIES)
            for i in range(count):
                pos = (random.randint(ENEMY_SCALE[0] // 2, SCREEN_WIDTH - ENEMY_SCALE[0] // 2), 0)
                new_enemy = enemy(pos, Judge)
                if new_enemy.rect.collidelist(Enemies) < 0:
                    Enemies.append(new_enemy)
        
        # Updates
        for st in Stars:
            st.update()

        Stars = list(filter(lambda st: st.valid, Stars))

        Player.update()
        for fire in Shots:
            fire.update()
        
        # Check if shots went out of view
        Shots = list(filter(lambda fire: fire.valid, Shots))

        # Check if enemies were hit by shots
        for ene in Enemies:
            ene.update()
            for fire in Shots:
                if ene.shotCollided(fire, GameScreen):
                    exp = explosion((ene.rect.centerx, ene.rect.centery))
                    Explosions.append(exp)
                    Enemies.remove(ene)
                    Shots.remove(fire)

        for exp in Explosions:
            exp.update()

        # Check the explosions
        Explosions = list(filter(lambda exp: exp.valid, Explosions)) 

        # Check if the enemies went out of view            
        Enemies = list(filter(lambda ene: ene.valid, Enemies))    

        # Check if the player jet collided with enemy
        for ene in Enemies:
            if Player.enemyCollided(ene):
                GameScreen.fill(DARK)
                Judge.endGame()
                pygame.display.update()
                FramePerSec.tick(FPS)

        # Update the screen
        GameScreen.fill(DARK)       # Clear Screen
        
        for st in Stars:
            st.draw(GameScreen)

        Player.draw(GameScreen)     # Player Jet

        for fire in Shots:
            fire.draw(GameScreen)   # Shots
        
        for ene in Enemies:
            ene.draw(GameScreen)    # Enemies

        for exp in Explosions:
            exp.draw(GameScreen)
        
        Judge.display()             # Score
        pygame.display.update()     # Update the screen
        
        FramePerSec.tick(FPS)       
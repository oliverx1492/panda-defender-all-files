
import math
from pickle import FALSE
import random
from tkinter import getboolean

import pygame
from pygame import mixer


pygame.init()

# screens
screen = pygame.display.set_mode((800, 600))
start_screen = pygame.display.set_mode((800,600))
game_over_screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('background_r.jpg')


# spped up
speeder = 1

# Icon
pygame.display.set_caption("Panda Defender")
icon = pygame.image.load('panda.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 350
playerY = 475
playerX_change = 0

#booster
boosterImg = []
boosterX = []
boosterY = []
boosterY_change = []


num_of_booster = 8

for i in range(num_of_booster):
    boosterImg.append(pygame.image.load('booster.png'))
    boosterX.append(random.randint(20,730))
    boosterY.append(random.randint(-5000,0))
    boosterY_change.append(0.5)


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(40)

# axe


axeImg = pygame.image.load('axe.png')
axeX = 0
axeY = 480
axeX_change = 0
axeY_change = 3
axe_state = "not-shooting"

# Score

score_value = 0
highscore = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 60)
over_font2 = pygame.font.Font('freesansbold.ttf', 29)
scoreover_font = pygame.font.Font('freesansbold.ttf', 40)

# Start Game
start_font = pygame.font.Font('freesansbold.ttf', 42)
# Title
title_font = pygame.font.Font('freesansbold.ttf', 55)
#highscore
hs_font = pygame.font.Font('freesansbold.ttf', 31)

def title_text():
    screen_title = title_font.render("PANDA DEFENDER", True, (255, 255, 255))
    screen.blit(screen_title, (150, 60))

def start_text():
    screen_start = start_font.render("PRESS S TO START THE GAME", True, (255, 255, 255))
    screen.blit(screen_start, (80, 250))

def get_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def display_new_highscore():
    new_highscore = hs_font.render("NEW HIGHSCORE!!!", True, (255,255,255))
    screen.blit(new_highscore, (80, 150))

def go_text():
    score_over = scoreover_font.render("FINAL SCORE: " + str(score_value), True, (255, 255, 255))
    screen.blit(score_over, (80, 50))

    screen_game_over = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(screen_game_over, (80, 250))

    screen_menu = over_font2.render("Press M to go back to the menu", True, (255,255,255))
    screen.blit(screen_menu, (80,350))

    screen_highscore = hs_font.render("Highscore: "  + str(highscore), True, (255,255,255))
    screen.blit(screen_highscore, (80, 450) )


def player(x, y):
    screen.blit(playerImg, (x, y))

def booster(x,y, i):
    screen.blit(boosterImg[i], (x,y))

def update_screen():
    pygame.display.update()


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def shooting_axe(x, y):
    global axe_state
    axe_state = "shooting"
    screen.blit(axeImg, (x, y))


def isCollision(enemyX, enemyY, axeX, axeY):
    distance = math.sqrt(math.pow(enemyX - axeX, 2) + (math.pow(enemyY - axeY, 2)))
    if distance < 27:
        return True
    else:
        return False


    

#start screen
starting = True
running = False
gameOver = False
getBooster = False
viewScore = True
newHighscore1 = False


while starting:
    running = False
    start_screen.fill((0,255,0))
    start_screen.blit(background, (0,0))
    start_text()
    title_text()
    update_screen()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            starting = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                running = True
                starting = False
                viewScore = True
                newHighscore1 = False
                update_screen()


                while running:

                    screen.fill((0, 0, 0))
                    # Background Image
                    screen.blit(background, (0, 0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

                        # chek if left / right
      

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                playerX_change = -2 * speeder
                            if event.key == pygame.K_RIGHT:
                                playerX_change = 2 * speeder
                            if event.key == pygame.K_SPACE:
                                if axe_state is "not-shooting":
                                    axeSound = mixer.Sound("throw.wav")
                                    axeSound.play()
                                    # 
                                    axeX = playerX
                                    shooting_axe(axeX, axeY)
                            if event.key == pygame.K_m:
                                        running = False  
                                        starting = True 
                                        score_value = 0
                                        for i in range(num_of_enemies):
                                            enemyX[i] = random.randint(0, 736)
                                            enemyY[i] = random.randint(50, 150)

                                            enemy(enemyX[i], enemyY[i], i)
                                        break
                        
                                

                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                playerX_change = 0

                

                    playerX += playerX_change
                    if playerX <= 0:
                        playerX = 0
                        
                    elif playerX >= 736:
                        playerX = 736
                    
                    # booster movement


                    # Enemy Movement
                    for i in range(num_of_enemies):

                        # Game Over
                        if enemyY[i] > 440:
                            
                            for j in range(num_of_enemies):
                                enemyY[j] = 1000 # enemy dissapears
                                
                                gameOver = True
                                viewScore = False
                                if score_value >= highscore:
                                    highscore = score_value
                                    newHighscore1 = True
                            if newHighscore1:
                                display_new_highscore()
                            go_text()
                            break
                                         

                        enemyX[i] += enemyX_change[i]
                        if enemyX[i] <= 0:
                            enemyX_change[i] = 1.2
                            enemyY[i] += enemyY_change[i]
                        elif enemyX[i] >= 736:
                            enemyX_change[i] = -1.2
                            enemyY[i] += enemyY_change[i]

                        # Collision
                        collision = isCollision(enemyX[i], enemyY[i], axeX, axeY)
                        if collision:
                            hitSound = mixer.Sound("hit.wav")
                            hitSound.play()
                            axeY = 480
                            axe_state = "not-shooting"
                            score_value += 1
                            enemyX[i] = random.randint(0, 736)
                            enemyY[i] = random.randint(50, 150)

                        enemy(enemyX[i], enemyY[i], i)
                    # booster appearing
                   
                    for i in range(num_of_booster):
                        booster(boosterX[i], boosterY[i],i)
                        boosterY[i] += boosterY_change[i]
                        boosterCollision = isCollision(playerX, playerY, boosterX[i], boosterY[i])
                        if boosterCollision:
                            boosterX[i] = random.randint(20,730)
                            boosterY[i] = random.randint(-4000,0)
                            speeder += 0.5
                        if gameOver:
                            boosterY[i] = 1000
                            


                    # axe Movement
                    if axeY <= 0:
                        axeY = 480
                        axe_state = "not-shooting"

                    if axe_state is "shooting":
                        shooting_axe(axeX, axeY)
                        axeY -= axeY_change

                    player(playerX, playerY)

                    
                    if viewScore:
                        get_score(textX, testY)
                    update_screen()
                                

                
                    
                    update_screen()


                # Game Loop ends



import pygame
import sys
import random 

#setting up the windows and initial setup

pygame.init() 
clock = pygame.time.Clock()

screenWidth = 1080
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pong")


#using "Rects"

ball = pygame.Rect(screenWidth/2 - 15, screenHeight/2 - 15, 30, 30)
player = pygame.Rect(screenWidth - 20, screenHeight/2 - 70, 10, 140)
opp = pygame.Rect(10, screenHeight/2 - 70, 10, 140)

#adding color

bgColor = pygame.Color('grey12')
lightGrey = (200, 200, 200)

#declaring the speeds

speedrange = [1, -1, 1.1, -1.1, 1.2, -1.2, 0.8, 0.9, -0.8, -0.9]

ballSpeedX = 7 * random.choice(speedrange)
ballSpeedY = 7 * random.choice(speedrange)
playerSpeed = 0
oppSpeed = 7



def ballAnim():
    global ballSpeedX, ballSpeedY
    #anims

    ball.x += ballSpeedX
    ball.y += ballSpeedY

    #making the walls bouncy

    if ball.top <= 0 or ball.bottom >= screenHeight:
        ballSpeedY *= -1
    if ball.left <= 0 or ball.right >= screenWidth:
        ballSpeedX *= -1
        ballRestart()

    #adding collisions

    if ball.colliderect(player) or ball.colliderect(opp):
        ballSpeedX *= -1

def playerAnim():

    player.y += playerSpeed

    #restricting player movement

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screenHeight:
        player.bottom = screenHeight

def oppAnim():
    if opp.top < ball.y:
        opp.top += oppSpeed
    if opp.bottom > ball.y:
        opp.bottom -= oppSpeed
    if opp.top <= 0:
        opp.top = 0
    if opp.bottom >= screenHeight:
        opp.bottom = screenHeight


def ballRestart():
    global ballSpeedX, ballSpeedY
    ball.center = (screenWidth/2, screenHeight/2)
    ballSpeedY *= random.choice(speedrange)
    ballSpeedX *= random.choice(speedrange)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerSpeed += 7
            if event.key == pygame.K_UP:
                playerSpeed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerSpeed -= 7
            if event.key == pygame.K_UP:
                playerSpeed += 7

    ballAnim()
    playerAnim()
    oppAnim()

    #adding the visuals

    screen.fill(bgColor)
    pygame.draw.rect(screen, lightGrey, player)
    pygame.draw.rect(screen, lightGrey, opp)
    pygame.draw.ellipse(screen, lightGrey, ball)
    pygame.draw.aaline(screen, lightGrey, (screenWidth/2,0), (screenWidth/2, screenHeight))


    pygame.display.flip()
    clock.tick(60)






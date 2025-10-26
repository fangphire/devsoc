import pygame
import sys
import random 

#setting up the windows and initial setup

pygame.init() 
clock = pygame.time.Clock()
pygame.mixer.init()

screenWidth = 1080
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pong")

#music

pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) 


#using "Rects"

ball = pygame.Rect(screenWidth/2 - 15, screenHeight/2 - 15, 30, 30)
player = pygame.Rect(screenWidth - 20, screenHeight/2 - 70, 10, 140)
opp = pygame.Rect(10, screenHeight/2 - 70, 10, 140)

#adding color

bgColor = pygame.Color('grey12')
lightGrey = (200, 200, 200)
white = (255, 255, 255)

#declaring the speeds

speedrange = [1, -1, 1.1, -1.1, 1.2, -1.2, 0.8, 0.9, -0.8, -0.9]

ballSpeedX = 7 * random.choice(speedrange)
ballSpeedY = 7 * random.choice(speedrange)
playerSpeed = 0
oppSpeed = 7

#scores

playerScore = 0
oppScore = 0
winningScore = 5

#game status
gameActive = True
gameFont = pygame.font.SysFont("comicsans", 60)



def ballAnim():
    global ballSpeedX, ballSpeedY, playerScore, oppScore, gameActive
    #anims

    ball.x += ballSpeedX
    ball.y += ballSpeedY

   # Wall collisions
    if ball.top <= 0 or ball.bottom >= screenHeight:
        ballSpeedY *= -1

    # Left/right collisions (score)
    if ball.left <= 0:
        playerScore += 1

        if playerScore >= winningScore:
            gameActive = False
        ballRestart()
    if ball.right >= screenWidth:
        oppScore += 1
        if oppScore >= winningScore:
            gameActive = False
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
    ballSpeedX = 7 * random.choice(speedrange)
    ballSpeedY = 7 * random.choice(speedrange)


def drawScore():
    playerText = gameFont.render(f"{playerScore}", True, lightGrey)
    oppText = gameFont.render(f"{oppScore}", True, lightGrey)
    screen.blit(playerText, (screenWidth/2 + 20, 20))
    screen.blit(oppText, (screenWidth/2 - 40, 20))


def gameOverScreen():
    screen.fill(bgColor)
    if playerScore >= winningScore:
        msg = "You Win!"
    else:
        msg = "You Lose!"
    text = gameFont.render(msg, True, white)
    restartText = gameFont.render("Press SPACE to Restart", True, white)
    screen.blit(text, (screenWidth/2 - text.get_width()/2, screenHeight/2 - 50))
    screen.blit(restartText, (screenWidth/2 - restartText.get_width()/2, screenHeight/2 + 50))
    pygame.display.flip()

def resetGame():
    global playerScore, oppScore, gameActive
    playerScore = 0
    oppScore = 0
    ballRestart()
    gameActive = True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if gameActive:
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
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    resetGame()

    if gameActive:
        ballAnim()
        playerAnim()
        oppAnim()

        #adding the visuals 

        screen.fill(bgColor)
        pygame.draw.rect(screen, lightGrey, player)
        pygame.draw.rect(screen, lightGrey, opp)
        pygame.draw.ellipse(screen, lightGrey, ball)
        pygame.draw.aaline(screen, lightGrey, (screenWidth/2, 0), (screenWidth/2, screenHeight))
        drawScore()
    else:
        gameOverScreen()


    pygame.display.flip()
    clock.tick(60)






#coding: utf8

import pygame, time, random

pygame.init()

def snake(headname, bodyname, snakeList, lead_x, lead_y):
    for XnY in snakeList:
        gameDisplay.blit(pygame.image.load(bodyname),(XnY[0],XnY[1]))
        gameDisplay.blit(pygame.image.load(headname),(lead_x,lead_y))

def message_to_screen(msg,color,x,y):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x,y])

white = (255,255,255)


display_width = 600
display_height = 600
block_size = 40

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Snake")

font = pygame.font.SysFont("Comicsans", 32)

gameExit = False

lead_x = (display_width-40)/2
lead_y = (display_height-40)/2
lead_x_change = 0
lead_y_change = 0

snakeList = []
snakeLength = 1
score = 0

appleX = round(random.randrange(block_size, display_width-block_size)/block_size)*block_size
appleY = round(random.randrange(block_size, display_height-block_size)/block_size)*block_size

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -block_size
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0

    if lead_x >= display_width-block_size or lead_x <0 or lead_y >= display_height-block_size or lead_y <0:
        gameDisplay.fill(white)
        message_to_screen(''.join(["Game over! Score: ",str(score)]), white, 200,260)
        pygame.display.update()
        time.sleep(2)
        gameExit = True

    # движение семьи
    lead_x += lead_x_change
    lead_y += lead_y_change
    snakeHead = [lead_x, lead_y]
    snakeList.append(snakeHead)
    if len(snakeList) > snakeLength:
        del snakeList[0]

    # столкновение с самой собой
    for eachSegment in snakeList[:-1]:
        if eachSegment == snakeHead:
            gameDisplay.blit(pygame.image.load('hone.webp'), (0, 0))
            message_to_screen(''.join(["Game over! Score: ",str(score)]), white, 200,260)
            pygame.display.update()
            time.sleep(2)
            gameExit = True

    # столкновение с грибом
    if lead_x == appleX and lead_y == appleY:
        appleX = round(random.randrange(block_size, display_width-block_size)/block_size)*block_size
        appleY = round(random.randrange(block_size, display_height-block_size)/block_size)*block_size
        snakeLength += 1
        score += 1

    gameDisplay.blit(pygame.image.load('hone.webp'), (0, 0))
    # отображение количества очков
    message_to_screen(''.join(["Score: ",str(score)]), white, 10,10)
    # отображение гриба
    gameDisplay.blit(pygame.image.load('grib.png'),(appleX, appleY))
    # отображение динозавров
    snake('joshi.jpg', 'joshi.jpg', snakeList, lead_x, lead_y)
    pygame.display.update()
    pygame.time.delay(150)

pygame.quit()
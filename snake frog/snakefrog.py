import pygame
import random

pygame.init()
height = 600
width = 800
white = 255,255,255
blue = 0,255,255
snake_x = 100
snake_y = 100
vel =5
move_x =0
move_y =0
snakelist = []
snakelength = 1
score_count = 0
def snake(snakelist):
    for i in range(len(snakelist)):
        pygame.draw.rect(screen,(0,0,0),(snakelist[i][0],snakelist[i][1],30,30))

frog = pygame.image.load('frog.png')
frog_x = random.randint(0,width-frog.get_width())
frog_y = random.randint(0,height-frog.get_height())
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("SnakeFrog")
music = pygame.mixer.Sound("sound115.wav")
clock = pygame.time.Clock()
def text(msg,color,text_x,text_y,size):
    font = pygame.font.SysFont("Arial", size,bold=False)
    a = font.render(msg,True,color)
    screen.blit(a,(text_x,text_y))
def game_end():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        text("Game Over",(0,0,0),250,200,45)
        pygame.display.update()


while True:
    clock.tick(100)
    screen.fill(white)
    pygame.draw.rect(screen,(0,0,0),(snake_x,snake_y,30,30))
    rect_1 = pygame.Rect(snake_x,snake_y,30,30)
    screen.blit(frog,(frog_x,frog_y))
    rect_2 = pygame.Rect(frog_x,frog_y,frog.get_width(),frog.get_height())
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

    if keys[pygame.K_LEFT]:
        move_x = -vel
        move_y = 0
    if keys[pygame.K_RIGHT]:
        move_x = vel
        move_y = 0
    if keys[pygame.K_UP]:
        move_x = 0
        move_y = -vel
    if keys[pygame.K_DOWN]:
        move_x = 0
        move_y = vel

    snake_x+= move_x
    snake_y+= move_y

    if snake_x > width:
        snake_x = -30
    elif snake_x<-30:
        snake_x = width
    elif snake_y>height:
        snake_y = -30
    elif snake_y<-30:
        snake_y = height

    if rect_1.colliderect(rect_2):
        frog_x = random.randint(0, width - frog.get_width())
        frog_y = random.randint(0, height - frog.get_height())
        snakelength+= 10
        music.play()
        score_count+= 1

    snakeHead = []
    snakeHead.append(snake_x)
    snakeHead.append(snake_y)
    snakelist.append(snakeHead)

    if len(snakelist)>snakelength:
        del snakelist[0]

    snake(snakelist)

    for j in snakelist[:-1]:
        if j == snakelist[-1]:
            game_end()
    b = "Your Score: "+str(score_count)
    text(b,(0,0,0),600,0,25)
    pygame.display.update()
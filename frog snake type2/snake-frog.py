import pygame
import random
import time
pygame.init()
font = pygame.font.SysFont("Times New Roman", 25)
score_read = open("snake-frog-score.txt",'r')
highest = score_read.read()
score_read.close()
highest = int(highest)

def textw(msg,color,text_x,text_y):
     text = font.render(msg, True, color)
     screen.blit(text,(text_x,text_y))

white=255,255,255
red = 255,0,0
blue = 0,255,255
width=1000
height= 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("SNAKE_FROG")
snake = pygame.image.load("snake2.png")
count_score = 0
fps = 100
frog = pygame.image.load("frog.png")
sound = pygame.mixer.Sound("sound115.wav")
sound_2 = pygame.mixer.Sound("sound116.wav")
back = pygame.image.load("game_bg.jpg")
x = 0
y = 0
move_x = 0
move_y = 0
vel = 5
frog_x = random.randint(0,width - frog.get_width())
frog_y = random.randint(0,height - frog.get_height())
count = 0
clock = pygame.time.Clock()


while True:
    clock.tick(fps)
    screen.fill(blue)
    textw('SNAKE-FROG',(0,0,0),350,0)
    screen.blit(frog,(frog_x,frog_y))



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                 move_x = vel
                 move_y = 0
            elif event.key == pygame.K_LEFT:
                 move_x = -vel
                 move_y = 0
            elif event.key == pygame.K_UP:
                 move_y = -vel
                 move_x = 0
            elif event.key == pygame.K_DOWN:
                 move_x = 0
                 move_y = vel
    screen.blit(snake, (x, y))
    snake_rec = pygame.Rect(x,y,150,155)
    frog_rec = pygame.Rect(frog_x,frog_y,frog.get_width(),frog.get_height())
    x += move_x
    y += move_y

    if x>width-160:
        move_x = -vel
        sound.play()
        count+=1
        
    elif x<0:
        move_x = vel
        sound.play()
        count += 1
    elif y>height-140:
        move_y = -vel
        sound.play()
        count += 1
    elif y<0:
        move_y = vel
        sound.play()
        count+=1


    if snake_rec.colliderect(frog_rec):
        frog_x = random.randint(0, width - frog.get_width())
        frog_y = random.randint(0, height - frog.get_height())
        sound_2.play()
        count_score+= 1
    if count_score>highest:
        textw("(NEW HIGHEST SCORE)",(255,0,0),290,50)
        score_file = open("snake-frog-score.txt","w")
        score_file.write(str(count_score))
        score_file.close()
    if count_score%5==0 and count_score!=0:
        fps+=0.10
        textw("Level increased",(0,0,255),300,300)


    a = "Remaining Life:"+str(3-count)
    textw(a,(0,0,0),800,0)
    b = "Your Score:"+str(count_score)
    textw(b,(0,0,0),840,30)
    c = "Previous Highest Score:"+str(highest)
    textw(c,(0,0,0),740,60)

    if count>2:
        textw("GAME OVER",(0,0,0),300,200)
        time.sleep(1)
        quit()




    pygame.display.update()
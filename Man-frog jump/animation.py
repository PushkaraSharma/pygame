import pygame
import random
pygame.init()

width = 852
height = 480
white = 255,255,255
x = 50
y = 410
frog_x = random.randint(150,800)
frog_y = 420
vel = 5
jump = False
jumpcount = 10
left = False
right = False
walkcount = 0
standing = True
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("ANIMATION")
pic_left = [pygame.image.load("L1.png"),pygame.image.load("L2.png"),pygame.image.load("L3.png"),pygame.image.load("L4.png"),pygame.image.load("L5.png"),pygame.image.load("L6.png"),pygame.image.load("L7.png"),pygame.image.load("L8.png"),pygame.image.load("L9.png")]
pic_right = [pygame.image.load("R1.png"),pygame.image.load("R2.png"),pygame.image.load("R3.png"),pygame.image.load("R4.png"),pygame.image.load("R5.png"),pygame.image.load("R6.png"),pygame.image.load("R7.png"),pygame.image.load("R8.png"),pygame.image.load("R9.png")]
standing_1 = pygame.image.load("standing.png")
bg = pygame.image.load("bg.jpg")
music = pygame.mixer.Sound("sound115.wav")
frog_1 =  pygame.image.load("frog.png")
frog_2 = pygame.image.load("frog.png")
clock = pygame.time.Clock()
frog_move = 10
count = 0


def charac():
    global walkcount
    screen.blit(bg,(0,0))
    #pygame.draw.rect(screen,(255,0,0),(x,y,64,64))
    if walkcount+1>=27:
        walkcount = 0
    if not(standing):
            if left:
                screen.blit(pic_left[walkcount//3],(x,y))
                walkcount+= 1
            elif right:
                screen.blit(pic_right[walkcount//3],(x,y))
                walkcount+= 1
    else:
        if right:
            screen.blit(pic_right[0],(x,y))
        elif left:
            screen.blit(pic_left[0],(x,y))
        else:
            screen.blit(standing_1,(x,y))


while True:
    clock.tick(50)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x<width-64:
        x+=vel
        right = True
        left = False
        standing = False
    elif keys[pygame.K_LEFT] and x>0:
        x-=vel
        right = False
        left = True
        standing = False
    else:
       # right = False
        #left = False
        standing = True
        walkcount = 0
    if not(jump):
        if keys[pygame.K_SPACE ]:
            music.play()
            jump = True
            left = False
            right = False
            walkcount = 0

    else:
        if jumpcount>= -10:
            n = 1
            if jumpcount<0:
                n = -1
            y-= (jumpcount**2)*0.5*n
            jumpcount-= 1
        else:
            jump = False
            jumpcount = 10

    charac()
    screen.blit(frog_1, (frog_x, frog_y))
    frog_x+=frog_move
    if frog_x>852-frog_1.get_width():
        frog_move = -10
    elif frog_x<0:
        frog_move = 10
    frg_rec = pygame.Rect(frog_x,frog_y,frog_1.get_width(),frog_1.get_height())
    man_rec = pygame.Rect(x,y,64,64)
    if frg_rec.colliderect(man_rec):
        music.play()
        frog_x = random.randint(150,800)
        count+= 1
    if count>2:
        quit()

    pygame.display.update()
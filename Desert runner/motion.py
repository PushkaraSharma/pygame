import pygame
import random
import time
pygame.init()

red = 255,0,0
width=500
height=650
b_x = 0
hero_x = 100
hero_y = 540
jump = False
jumpcount = 10
walkcount = 30
n_x = 500
n_y = 580
count = 0
score_count = 0
FPS = 45
font = pygame.font.SysFont("Times New Roman", 25,bold=True,italic=True)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Runner")
bg = pygame.image.load("bg4.jpg")
music = pygame.mixer.Sound('Lounge Game2.wav')

music_2 = pygame.mixer.Sound('sound115.wav')
hero = [pygame.image.load("spr1.png"),pygame.image.load("spr2.png"),pygame.image.load("spr3.png"),pygame.image.load("spr4.png"),
        pygame.image.load("spr5.png"),pygame.image.load("spr6.png"),pygame.image.load("spr7.png"),pygame.image.load("spr8.png"),
        pygame.image.load("spr9.png"),pygame.image.load("spr10.png")]
obs = [pygame.image.load("obs1.png"),pygame.image.load("obs2.png"),pygame.image.load("obs3.png"),pygame.image.load("obs4.png")]
starting_bg = pygame.image.load("starting1.png")
staring_button = pygame.image.load("starting2.png")
starting_end = pygame.image.load("starting3.png")
select = random.randrange(0,4)
clock = pygame.time.Clock()

read_jump_score = open("runner_desert.txt",'r')
highest_score = read_jump_score.read()
read_jump_score.close()
highest_score = int(highest_score)

def text(msg,color,text_x,text_y):
    write_text = font.render(msg,True,color)
    screen.blit(write_text,(text_x,text_y))


def body():

    global b_x
    global walkcount
    rel_x = b_x%1000
    screen.blit(bg,(rel_x-1000,-300))
    if rel_x<width:
        screen.blit(bg,(rel_x,-300))
    b_x-= 1

    if jump:
        screen.blit(hero[9],(hero_x,hero_y))
    else:
        if walkcount + 1 > 30:
            walkcount = 0
        screen.blit(hero[walkcount // 3], (hero_x, hero_y))
        walkcount += 1

def end_game():
    pygame.mixer.pause()
    text("GAME OVER",(255,0,0),150,250)
    time.sleep(2)
    start_menu()


    pygame.display.update()



def game_body():
    music.play(-1)
    global FPS,hero_x,hero_y,count,score_count
    global jump,select,n_y,n_x,b_x,jumpcount
    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and hero_x<width-83:
            hero_x+= 2
        if keys[pygame.K_LEFT] and hero_x>0:
            hero_x-= 2
        else:
            pass

        if not(jump):
            if keys[pygame.K_SPACE]:
                jump = True
                music_2.play()


        else:
            if jumpcount>= -10:
                n = 1
                if jumpcount<0:
                    n = -1
                hero_y-= (jumpcount**2)*0.5*n
                jumpcount-= 1
            else:
                jump = False
                jumpcount = 10

        body()
        text("DESERT RUNNER",(0,0,0),100,0)
        hero_rec = pygame.Rect(hero_x,hero_y,70,80)
        screen.blit(obs[select],(n_x,n_y))
        obs_rec = pygame.Rect(n_x, n_y, 20, 80)
        n_x -= 10
        if n_x < -80:
            n_x = 500
            select = random.randrange(0, 4)

        if hero_rec.colliderect(obs_rec):
            count+= 1
            n_x = -70
        if n_x == 0:
            score_count+=1
        if score_count%10 == 0 and score_count!= 0:
            FPS+=0.1
            text("LEVEL UP",(0,0,255),200,250)
        if score_count>highest_score:
            text("NEW HIGHEST SCORE",(255,0,0),125,150)
            jump_score = open("runner_desert.txt", 'w')
            jump_score.write(str(score_count))
            jump_score.close()

        life = "Remaining Life: "+str(3-count)
        score = "Your Score: "+str(score_count)
        text(life,(0,0,0),300,50)
        text(score,(0,0,0),300,100)

        if count>2:
            end_game()
        pygame.display.update()

def start_menu():
    parameters()

    while True:
        screen.blit(starting_bg,(0,0))
        screen.blit(staring_button,(300,200))
        screen.blit(starting_end,(280,300))
        text("DESERT RUNNER",(255,0,0),50,100)
        keys = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 300+175>keys[0]>300 and 200+82>keys[1]>200:
            if click[0]==1:
                game_body()
        elif 280+200>keys[0]>280 and 300+52>keys[1]>300:
            if click[0]==1:
                quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()

def parameters():
    global b_x,hero_x,hero_y,jumpcount,jump,walkcount,n_x,n_y,count,score_count
    global bg,music,music_2,select,clock
    b_x = 0
    hero_x = 100
    hero_y = 540
    jump = False
    jumpcount = 10
    walkcount = 30
    n_x = 500
    n_y = 580
    count = 0
    score_count = 0
    bg = pygame.image.load("bg4.jpg")
    music = pygame.mixer.Sound('Lounge Game2.wav')

    music_2 = pygame.mixer.Sound('sound115.wav')
    select = random.randrange(0, 4)
    clock = pygame.time.Clock()


start_menu()

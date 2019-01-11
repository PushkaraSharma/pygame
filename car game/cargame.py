import pygame
import random
import time
pygame.init()
width = 840
height = 650
b_y = 0
car_x =300
car_y = 560
move_cx = 0
move_cy = 0
car_vel = 10
screen = pygame.display.set_mode((width,height))
bg = pygame.image.load("road.png")
carleft = pygame.image.load("carleft.png")
carright = pygame.image.load("carright.png")
car = pygame.image.load("car.png")
oppcar = [pygame.image.load("car1.png"),pygame.image.load("car2.png"),pygame.image.load("car3.png"),pygame.image.load("car4.png"),
          pygame.image.load("car5.png"),pygame.image.load("car6.png"),pygame.image.load("car7.png")]
startbg = pygame.image.load("bgstart.png")
start_pic = pygame.image.load("starting2.png")
end_pic = pygame.image.load("starting3.png")
select1 = random.randint(0,6)
select2 = random.randint(0,6)
select3 = random.randint(0,6)
select4 = random.randint(0,6)
left = False
right = False
straight = True
car1x = random.randrange(140,640)
car2x = random.randrange(140,640)
car3x = random.randrange(140,640)
car4x = random.randrange(140,640)
car1y = -120
car2y = -280
car3y = -400
car4y = -530
car_count = 0
clock = pygame.time.Clock()

def text(msg,fontsize,color,text_x,text_y):
    font = pygame.font.SysFont("Arial",fontsize,bold=True)
    write = font.render(msg,True,color)
    screen.blit(write,(text_x,text_y))

def character():
    global b_y
    #moving background
    rel_y = b_y%650
    screen.blit(bg,(0,rel_y-650))
    if rel_y<height:
        screen.blit(bg,(0,rel_y))
    b_y+=3

    if straight:
        screen.blit(car,(car_x,car_y))
    elif left:
        screen.blit(carleft,(car_x,car_y))
    elif right:
        screen.blit(carright,(car_x,car_y))

def oppcars():
    global car1x, car2x, car3x, car4x, car2y, car3y, car1y,car4y, select1, select2, select3,select4,car_count
    screen.blit(oppcar[select1],(car1x,car1y))
    if car1y == 720:
        car1y = -120
        car1x = random.randrange(140,640)
        select1 = random.randint(0,6)
        car_count+=1
    car1y+= 5
    screen.blit(oppcar[select2],(car2x,car2y))
    if car2y == 650:
        car2y = -240
        car2x = random.randrange(140,640)
        select2 = random.randint(0,6)
        car_count += 1
    car2y+= 5
    screen.blit(oppcar[select3], (car3x, car3y))
    if car3y == 650:
        car3y = -360
        car3x = random.randrange(140, 640)
        select3 = random.randint(0, 6)
        car_count += 1
    car3y += 5
    screen.blit(oppcar[select4], (car4x, car4y))
    if car4y == 650:
        car4y = -470
        car4x = random.randrange(140, 640)
        select4 = random.randint(0, 6)
        car_count += 1
    car4y += 5
    a = "Score: " + str(car_count)
    text(a, 25, (255, 0, 0,), 730, 0)
    pygame.display.update()

def game():
    global car_x,car_y,move_cx,move_cy,right,left,straight,car_vel
    while True:
        clock.tick(100)

        character()
        oppcars()

        car_x+= move_cx
        car_y-= move_cy
        #screen.blit(bg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_cx = -car_vel
                    left = True
                    right = False
                    straight = False
                elif event.key ==  pygame.K_RIGHT:
                    move_cx = car_vel
                    left = False
                    right = True
                    straight = False
            if event.type == pygame.KEYUP:
                straight = True
                move_cx = 0

        if car_x<140:
            move_cx = 1
        elif car_x>650:
            move_cx = -1
        #collides
        car_rec = pygame.Rect(car_x, car_y, 55, 81)
        rec1 = pygame.Rect(car1x, car1y, 47, 95)
        rec2 = pygame.Rect(car2x, car2y, 47, 95)
        rec3 = pygame.Rect(car3x, car3y, 47, 95)
        if car_rec.colliderect(rec1) or car_rec.colliderect(rec2) or car_rec.colliderect(rec3):
            #text("Game Over",45,(0,0,0),300,400)
            time.sleep(2)
            game_end()
    pygame.display.update()

def start_window():
    parameters()
    while True:

        screen.blit(startbg,(0,0))
        screen.blit(start_pic,(330,160))
        screen.blit(end_pic,(310,500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 330+175>pos[0]>330 and 160+82>pos[1]>160:
            if click[0]==1:
                game()
        elif 310+200>pos[0]>310 and 500+52>pos[1]>500:
            if click[0]==1:
                quit()
        pygame.display.update()
def game_end():
    time.sleep(1)
    start_window()
    pygame.display.update()
def parameters():
    global b_y,car,car_vel,car_count,car4y,car4x,car1x,car1y,car2x,car2y,car3y,car3x,car4x,car4y,move_cy,move_cx,car_x,car_x,carleft,carright
    global bg,oppcar,select3,select1,select2,select4,left,right,straight
    b_y = 0
    car_x = 300
    car_y = 560
    move_cx = 0
    move_cy = 0
    car_vel = 10
    bg = pygame.image.load("road.png")
    carleft = pygame.image.load("carleft.png")
    carright = pygame.image.load("carright.png")
    car = pygame.image.load("car.png")
    oppcar = [pygame.image.load("car1.png"), pygame.image.load("car2.png"), pygame.image.load("car3.png"),
              pygame.image.load("car4.png"),
              pygame.image.load("car5.png"), pygame.image.load("car6.png"), pygame.image.load("car7.png")]

    select1 = random.randint(0, 6)
    select2 = random.randint(0, 6)
    select3 = random.randint(0, 6)
    select4 = random.randint(0, 6)
    left = False
    right = False
    straight = True
    car1x = random.randrange(140, 640)
    car2x = random.randrange(140, 640)
    car3x = random.randrange(140, 640)
    car4x = random.randrange(140, 640)
    car1y = -120
    car2y = -280
    car3y = -400
    car4y = -530
    car_count = 0


start_window()

import pygame
import random

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
class App:
    pass
app = App()

air = 0
app.x = 50
app.y = 350
app.projx = 450
app.projy = 350
app.prox = 450
app.proy = 350
app.px = 450
app.py = 350
app.dx = 450
app.dy = 50
time = 0
gtime = 0
speed = 0 + (gtime)
run = True 
safe = True
com = 1
#definitions
def flyer():
    app.prox -= 4
    if app.prox < 150:
        app.proy -= 4 + speed
        app.prox -= 2 + speed
def standerd():
        app.projx -= 3 + speed
def fast():
    app.px -= 6 + speed
def diver():
    if app.dx <= 3:
         pass
def middle():
    pass
#generate assets
penguin = pygame.image.load('sawczak_demo/assets/penguin.png')
penguin = pygame.transform.scale(penguin , (50,50))
ice = pygame.image.load('sawczak_demo/assets/iceberg.png')
ice = pygame.transform.scale(ice , (50,100 ))

#main loop
while run:
    #speed up
    gtime += 1
    speed += (gtime /  700000)
    #what level is the speed at
    level = int(speed // 1 + 1)

    clock.tick(120)
    #check if they quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    #keys means if a key is pressed
    keys = pygame.key.get_pressed()   

    #reset the projectiles
    if app.projx < 0:
        app.projx = 450
        app.proy = 350
        com = 1
    if app.prox < -20:
        app.prox = 450
        app.proy = 350
        com = 1
    if app.px < -20:
        app.px = 450
        com = 1
    
    #making the projictle move and projectile movement
    if com == 1:
        com = 0
        #if level == 1:
            #a = 0
        #elif level == 2:
            #a = random.randint(0,1)
        #elif level >= 3:
        a = random.randint(0,2)
        #else: TODO
         #   a = random.randint(0,4)
    if a == 0:
        standerd()
    elif a == 1:
        fast()
    elif a == 2:
        flyer()
    elif a == 3:
        if app.dx > 150:
            app.dx -= 2 + speed
        elif app.dx > 100:
            pass   
    elif a == 4:
        pass

    #calculate air time to incrase the fall speed
    if app.y < 350:
        air += 0.07
    if app.y == 350:
        air = 0
    
    #track the inputs
    if keys[pygame.K_SPACE]:
        if app.y < 50:
            pass
        elif time <= 25:
            app.y -= 6 + speed / 2 - air
            time += 1
        elif app.y < 350: 
            app.y += 5 + speed / 2 + air
    elif app.y < 350:
        app.y += 5 + speed / 2 + air
    
    if app.y > 350:
        app.y = 350

    if app.y  == 350:
        if time > 0:
            time -= 1
    if app.x - app.projx < 25 and app.x - app.projx > -25 and app.y - app.projy < 25 and app.y - app.projy > -25:
        break
    if app.x - app.prox < 35 and app.x - app.prox > -35 and app.y - app.proy < 35 and app.y - app.proy > -35:
        break
    if app.x - app.px < 25 and app.x - app.px > -25 and app.y - app.py < 25 and app.y - app.py > -25:
        break
 
    #drawings
    window.fill((0, 0, 64))
    window.blit(penguin, (app.x - 30  , app.y - 30))
    window.blit (ice, (app.projx - 30  , app.projy - 55))
    # pygame.draw.circle(window, 'red' , (app.projx , app.projy) , 20)
    pygame.draw.circle(window, 'green' , (app.px , app.py) , 20)
    pygame.draw.circle(window, 'purple' , (app.prox , app.proy) , 20)
    pygame.draw.rect(window, 'gray', (0, 365, 400, 400))
 
    #jump meater
    pygame.draw.rect(window , 'gray' , (0,0, 100 , 40))
    if time <= 30:
        pygame.draw.rect(window , 'red' , (5,5,5,30)) 
    if time <= 27:
        pygame.draw.rect(window, 'red' , (10,5,10,30))
    if time <= 24:
        pygame.draw.rect(window, 'red' , (15,5,15,30))
    if time <= 21:
        pygame.draw.rect(window, 'orange' , (20,5,20,30))
    if time <= 18:
        pygame.draw.rect(window, 'orange' , (25,5,25,30))
    if time <= 15:
        pygame.draw.rect(window, 'orange' , (30,5,30,30))
    if time <= 12:
        pygame.draw.rect(window, 'yellow' , (35,5,35,30))
    if time <= 9:
        pygame.draw.rect(window, 'yellow' , (40,5,40,30))
    if time <= 6:
        pygame.draw.rect(window, 'yellow' , (45,5,45,30))
    if time <= 3:
        pygame.draw.rect(window, 'green' , (50,5,40,30))
    if time <= 0:
        pygame.draw.rect(window, 'green' , (55 , 5 , 40 , 30))
    #making a score board
    font = pygame.font.SysFont('New times roman', 24)
    app.text = font.render(f'level; {level}', True, 'white', '#000064')
    window.blit(app.text , (100,375))

    pygame.display.flip()
pygame.quit()
exit()
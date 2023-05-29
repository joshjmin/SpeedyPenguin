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
time = 0
run = True
safe = True
com = 1
#definitions
def flyer():
    app.prox -= 2
    if app.prox < 100:
        app.proy -= 4
        app.prox -= 4

def standerd():
        app.projx -= 3

def fast():
    app.px -= 6

# #from sawczak_demo import image 


# #image = image.open('sawczak_demo.penguin.png')

#new_image = image.resize((500, 500))
#new_image.save('myimage_500.jpg')

penguin = pygame.image.load('sawczak_demo/assets/penguin.png')
penguin = pygame.transform.scale(penguin , (50,100 ))
# new_image = image.resize((500, 500))
# new_image.save('myimage_500.jpg')

while run:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    keys = pygame.key.get_pressed()    
    #make the projectile
    if com == 1:
        a = random.randint(0,2)
    #reset the projectiles
    if app.projx < -20:
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
    
    #making the projictle moove
    if com == 1:
        com = 0
        a = random.randint(0,2)
    if a == 0:
        app.projx -= 3
    elif a == 1:
        app.px -= 6
    else:
        #flyer
        app.prox -= 4
        if app.prox < 150:
            app.proy -= 4
            app.prox -= 2

    #calculate air time to incrase the fall speed
    if app.y < 350:
        air += 0.07
    if app.y == 350:
        air = 0
    
    #track the inputs
    if keys[pygame.K_SPACE]:
        if app.y < 50:
            pass
        elif time <= 30:
            app.y -= 5 - air
            time += 1
        elif app.y < 350: 
            app.y += 3 + air
    elif app.y < 350:
        app.y += 3 + air
    
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
    window.blit(penguin, (app.x - 20  , app.y - 75))
    pygame.draw.circle(window, 'red' , (app.projx , app.projy) , 20)
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
    pygame.display.flip()
pygame.quit()
exit()
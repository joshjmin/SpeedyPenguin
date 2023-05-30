#imports
import pygame
import random
from time import sleep
class App:
    pass
app = App()

def set_ping(event) -> None:
    app.ping_pos = pygame.mouse.get_pos()    

def opening_screen():

# Set up the window
    pygame.init()
    pygame.display.set_caption('press the button to play')
    app.ping_pos = [0,0]
   
#opening screen
    running = True
    while running:
        window = pygame.display.set_mode([200, 200])
        pygame.draw.rect(window , 'gray' , (0,0,200,200))
        font3 = pygame.font.SysFont('New times roman', 24)
        app.text3 = font3.render(f'click me to play', True, '#0000FF', '#A5F2F3')
        window.blit(app.text3 , (75,125))
        
        for event in pygame.event.get():

        # User clicks window close button
            if event.type == pygame.QUIT:
                running = False
        
        # A mouse button is pressed down
            elif event.type == pygame.MOUSEBUTTONDOWN:
                set_ping(event)
        print(app.ping_pos)
        if app.ping_pos[0] > 70 and app.ping_pos[0] < 190 and app.ping_pos[1] < 111 and app.ping_pos[1] > 154:
            running = False
    # Update the display
        pygame.display.flip()

# Quit the window
    pygame.quit()

opening_screen()

#start window and other starting actions
pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
class App:
    pass
app = App()
#making placements and terms


air = 0
app.p_x = 50
app.p_y = 350
app.standerdx = 450
app.standerdy = 350
app.flyerx = 450
app.flyery = 350
app.fastx = 450
app.fasty = 350
app.diverx = 450
app.divery = 50
app.middlex = 450
app.middley = 330
app.uperx = 500
app.upery = 500
leveling = False

time = 0
gtime = 0
speed = 0 + (gtime)

run = True 
com = 1
motion = 'standing'
frame = 0

#definitions
def flyer():
    app.flyerx -= 4 + speed
    if app.flyerx < 150:
        app.flyery -= 4 + speed
        app.flyerx -= 2 + speed
def standerd():
        app.standerdx -= 3 + speed
def fast():
    app.fastx -= 6 + speed
def diver():
    if app.divery <= 325:
        app.divery += 3 +speed
    app.diverx -= 2 + speed
    app.uperx = app.diverx 
    app.upery = app.divery - 30
def middle():
    app.middlex -= 3 + speed
    app.uperx = app.middlex 
    app.upery = app.middley - 30
def reset():
    air = 0
    app.x = 50
    app.y = 350
    app.standerdx = 450
    app.standerdy = 350
    app.flyerx = 450
    app.flyery = 350
    app.fastx = 450
    app.fasty = 350
    app.diverx = 450
    app.divery = 50
    app.middlex = 450
    app.middley = 330
    app.uperx = 500
    app.upery = 500
    speed = 0
    sleep(1)

#generate assets
penguin = pygame.image.load('src/assets/penguin<3.png')    
penguin = pygame.transform.scale(penguin , (50,50))
ice = pygame.image.load('sawczak_demo/assets/iceberg.png')
ice = pygame.transform.scale(ice , (100,90 ))

#main loop
while run:
    #ticks and frame data
    clock.tick(120)
    #collect fram data
    frame += 1
    if frame == 4:
        frame = 1
    #speed up
    gtime += 1
    speed += (gtime /  5000000)
    #what level is the speed at
    level = int((gtime // 1000) + 1)
    
    #check if they quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    #reset the projectiles
    if app.standerdx < 0:
        app.standerdx = 450
        com = 1
    if app.flyerx < -20:
        app.flyerx = 450
        app.flyery = 350
        com = 1
    if app.fastx < -20:
        app.fastx = 450
        com = 1
    if app.diverx <= -20: 
        app.diverx = 450
        app.divery = 0
        com = 1
    if app.middlex <= -20:
        app.middlex = 450
        com = 1
    
    #making the projictle move and projectile movement
    if com == 1:
        com = 0
        if leveling == True:
            if level == 1:
                a = random.randint(0,1)
            elif level == 2:
                a = random.randint(0,2)
            elif level >= 3:
                a = random.randint(0,4)
            else:
                a = random.randint(0,4)
        else:
            a = random.randint(0,4)
    if a == 0:
        standerd()
    elif a == 2:
        fast()
    elif a == 3:
        flyer()
    elif a == 4:
        diver()
    elif a == 1:
        middle()

    #calculate air time to incrase the fall speed
    if app.p_y < 350:
        air += 0.07
    if app.p_y == 350:
        air = 0
    
    #track inputs
    #keys means if a key is pressed
    keys = pygame.key.get_pressed()   
    #what to do if preseed
    if keys[pygame.K_UP] or keys[pygame.K_SPACE]  or keys[pygame.K_w]:
        if app.p_y < 50:
            pass
        elif time <= 20:
            app.p_y -= 6 + speed / 2 - air
            time += 1
            motion = 'jumping'
        elif app.p_y < 350: 
            app.p_y += 5 + speed / 2 + air
            motion = 'jumping'
    elif app.p_y < 350:
        app.p_y += 5 + speed / 2 + air
        motion = 'jumping'
    
    if app.p_y > 350:
        app.p_y = 350
    
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if app.p_y < 349:
            pass
        else:
            if app.p_y >= 360:
                app.p_y = 360
            app.p_y += 5
            motion = 'sliding'
    elif app.p_y > 360:
        app.p_y = 350

    if app.p_y == 350:
        motion = 'standing'

    #recahrge jump power
    if app.p_y  == 350:
        if time > 0:
            time -= 1

    #check for collisions
    if app.p_x - app.standerdx < 25 and app.p_x - app.standerdx > -25 and app.p_y - app.standerdy < 25 and app.p_y - app.standerdy > -25:
        gtime = 0
        reset()
    if app.p_x - app.flyerx < 35 and app.p_x - app.flyerx > -35 and app.p_y - app.flyery < 35 and app.p_y - app.flyery > -35:
        gtime = 0
        reset()
    if app.p_x - app.fastx < 25 and app.p_x - app.fastx > -25 and app.p_y - app.fasty < 25 and app.p_y - app.fasty > -25:
        gtime = 0
        reset()
    if app.p_x - app.diverx < 25 and app.p_x - app.diverx > -25 and app.p_y - app.divery < 25 and app.p_y - app.divery > -25:
        gtime = 0
        reset()
    if app.p_x - app.middlex < 25 and app.p_x - app.middlex > -25 and app.p_y - app.middley < 25 and app.p_y - app.middley > -25:
        gtime = 0
        reset()
    if app.p_x - app.uperx < 25 and app.p_x - app.uperx > -25 and app.p_y - app.upery < 25 and app.p_y - app.upery > -25:
        gtime = 0
        reset()

    #drawings
    #TODO make animation for the walking of the main player
    #make the backround #TODO better
    window.fill((0, 0, 64))
    #draw the charecters
    window.blit(penguin, (app.p_x - 30  , app.p_y - 30))
    window.blit (ice, (app.standerdx - 50  , app.standerdy - 35))
    pygame.draw.circle(window, 'green' , (app.fastx , app.fasty) , 20)
    pygame.draw.circle(window, 'purple' , (app.flyerx , app.flyery) , 20)
    pygame.draw.rect(window, '#A5F2F3', (0, 365, 400, 400))
    pygame.draw.circle(window , 'yellow' , (app.diverx , app.divery) , 20)
    pygame.draw.circle(window , 'brown' , (app.middlex , app.middley) , 20)
    if app.uperx == app.middlex:
        pygame.draw.circle(window , 'brown' , (app.uperx , app.upery) , 20)
    elif app.uperx == app.diverx:
        pygame.draw.circle(window , 'yellow' , (app.uperx , app.upery) , 20)
 
    #jump meter
    pygame.draw.rect(window , 'gray' , (0,0, 100 , 40))
    if time <= 20:
        pygame.draw.rect(window , 'red' , (5,5,5,30)) 
    if time <= 18:
        pygame.draw.rect(window, 'red' , (10,5,10,30))
    if time <= 16:
        pygame.draw.rect(window, 'red' , (15,5,15,30))
    if time <= 14:
        pygame.draw.rect(window, 'orange' , (20,5,20,30))
    if time <= 12:
        pygame.draw.rect(window, 'orange' , (25,5,25,30))
    if time <= 10:
        pygame.draw.rect(window, 'orange' , (30,5,30,30))
    if time <= 8:
        pygame.draw.rect(window, 'yellow' , (35,5,35,30))
    if time <= 6:
        pygame.draw.rect(window, 'yellow' , (40,5,40,30))
    if time <= 4:
        pygame.draw.rect(window, 'yellow' , (45,5,45,30))
    if time <= 2:
        pygame.draw.rect(window, 'green' , (50,5,40,30))
    if time <= 0:
        pygame.draw.rect(window, 'green' , (55 , 5 , 40 , 30))
    #making a score board
    font = pygame.font.SysFont('New times roman', 24)
    app.text = font.render(f'LEVEL: {level}', True, '#0000FF', '#A5F2F3')
    window.blit(app.text , (300,375))
    #score
    font_2 = pygame.font.SysFont('New times roman', 24)
    app.text_2 = font_2.render(f'score: {gtime}', True, '#0000FF', '#A5F2F3')
    window.blit(app.text_2 , (100,375))
    pygame.display.flip()
pygame.quit()
exit()
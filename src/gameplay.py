class App:
    pass
app = App()
import pygame
from set_mode import difficulty

"""
This code runs the main function of the game 
such as setting up speed 
(and how it increases as level goes up)
obstacles (2x for jumping, 1x for sliding, 1x for jump or slide, 1x flying).
This code also takes the difficuly setting
chosen by the user and models the
speed and jump after that choice.
The code also messures score based on distance/level and 
displays it on the lower bar.
It also imports 3 types of penguin (standing, sliding and flying)
and changes the users icon based of the keys pressed.

"""

def gameplay():
    #imports
    import random
    from time import sleep

    #start window and other starting actions
    pygame.init()
    window = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Enter the Name of the game')
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

    time = 0
    gtime = 0
    speed = 0 + (gtime * (1.1))

    com = 1
    motion = 'standing'
    frame = 0
    mode = 0
    mode = difficulty()
    def reset():
        sleep(1)
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

        time = 0
        gtime = 0
        speed = 0 + (gtime)
        com = 1
        motion = 'standing'
        frame = 0
        active = False
    #definitions
    def flyer():
        app.flyerx -= 4 + speed - mode
        if app.flyerx < 150:
            app.flyery -= 4 + speed - mode
            app.flyerx -= 2 + speed - mode
    def standerd():
        app.standerdx -= 3 + speed - mode
    def fast():
        app.fastx -= 6 + speed - mode
    def diver():
        if app.divery <= 325:
            app.divery += 3 + speed - mode
        app.diverx -= 2 + speed - mode
        app.uperx = app.diverx 
        app.upery = app.divery - 30
    def middle():
        app.middlex -= 3 + speed - mode
        app.uperx = app.middlex 
        app.upery = app.middley - 30

    #generate assets
    if mode == 1:
        penguin = pygame.image.load('src/assets/penguin_standing.png')    
        penguin = pygame.transform.scale(penguin , (40,50))
        penguin_jump = pygame.image.load('src/assets/flyingpenguin(pink).png')
        penguin_jump = pygame.transform.scale(penguin_jump , (50 , 50))
        penguin_slide = pygame.image.load('src/assets/penguin_sliding(pink).png')
        penguin_slide = pygame.transform.scale(penguin_slide , (40,40))
    elif mode == 0:
        penguin = pygame.image.load('src/assets/penguin_standing(normal).png')    
        penguin = pygame.transform.scale(penguin , (40,50))
        penguin_jump = pygame.image.load('src/assets/flyingpenguin(normal).png')
        penguin_jump = pygame.transform.scale(penguin_jump , (50 , 50))
        penguin_slide = pygame.image.load('src/assets/penguin_sliding(normal).png')
        penguin_slide = pygame.transform.scale(penguin_slide , (40,40))
    else:
        penguin = pygame.image.load('src/assets/penguin_standing(hard).png')    
        penguin = pygame.transform.scale(penguin , (40,50))
        penguin_jump = pygame.image.load('src/assets/flyingpenguin(hard).png')
        penguin_jump = pygame.transform.scale(penguin_jump , (50 , 50))
        penguin_slide = pygame.image.load('src/assets/penguin_sliding(hard).png')
        penguin_slide = pygame.transform.scale(penguin_slide , (40,40))
    
    ice = pygame.image.load('sawczak_demo/assets/iceberg.png')
    ice = pygame.transform.scale(ice , (100,90 ))
    ice2 = pygame.image.load('src/assets/isicle.png')    
    ice2 = pygame.transform.scale(ice2 , (30,30))
    ice2 = pygame.transform.rotate(ice2 , 270)
    active = True
    #main loop 
    while active:
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
                exit()

        #reset the projectiles
        if app.standerdx < -20:
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
            #set restrictions based on level
            if level == 1:
                a = random.randint(0,1)
            elif level == 2:
                a = random.randint(0,2)
            elif level >= 3:
                a = random.randint(0,4)
        #make standered iceberg move
        if a == 0:
            app.standerdx -= 3 + speed - mode
        #make fast move
        elif a == 2:
            app.fastx -= 5 + speed - mode
        #make the faker move
        elif a == 3:
            app.flyerx -= 3 + speed - mode
            if app.flyerx < 150:
                app.flyery -= 4 + speed - mode
                app.flyerx -= 2 + speed - mode
        #make the diver move
        elif a == 4:
            if app.divery <= 325:
                app.divery += 4 + speed - mode
            app.diverx -= 4 - mode
            app.uperx = app.diverx 
            app.upery = app.divery - 30
            if app.divery > 325:
                app.divery = 325
        #make the middle slider
        elif a == 1:
            app.middlex -= 3 + speed - mode
            app.uperx = app.middlex 
            app.upery = app.middley - 30

        #calculate air time to incrase the fall speed
        if app.p_y < 350:
            air += 0.13
        if app.p_y == 350:
            air = 0

        #track inputs
        #keys means if a key is pressed
        keys = pygame.key.get_pressed()   
        #what to do if preseed
        #Jumping
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]  or keys[pygame.K_w]:
            #max hight
            if app.p_y < 50:
                time += 0.7 - mode / 3
                app.p_y += 10
            #restrictions based on time jumping
            elif time <= 23:
                app.p_y -= 6 + speed / 2 - air
                time += 0.7 - mode / 3
                motion = 'jumping'
            elif app.p_y < 350: 
                app.p_y += 5 + speed / 2 + air
                motion = 'jumping'
        elif app.p_y < 350:
            app.p_y += 5 + speed / 2 + air
            motion = 'jumping'
        #reset to bace level
        if app.p_y > 350:
            app.p_y = 350
        #code for how to slide
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
        if app.p_y  >= 350:
            if time > 0:
                time -= 1

        #check for collisions
        if app.p_x - app.standerdx < 25 and app.p_x - app.standerdx > -25 and app.p_y - app.standerdy < 25 and app.p_y - app.standerdy > -25:
            reset()
            return gtime
        if app.p_x - app.flyerx < 35 and app.p_x - app.flyerx > -35 and app.p_y - app.flyery < 35 and app.p_y - app.flyery > -35:
            reset()
            return gtime
        if app.p_x - app.fastx < 25 and app.p_x - app.fastx > -25 and app.p_y - app.fasty < 25 and app.p_y - app.fasty > -25:
            reset()
            return gtime
        if app.p_x - app.diverx < 25 and app.p_x - app.diverx > -25 and app.p_y - app.divery < 25 and app.p_y - app.divery > -25:
            reset()
            return gtime
        if app.p_x - app.middlex < 25 and app.p_x - app.middlex > -25 and app.p_y - app.middley < 25 and app.p_y - app.middley > -25:
            reset()
            return gtime
        if app.p_x - app.uperx < 25 and app.p_x - app.uperx > -25 and app.p_y - app.upery < 25 and app.p_y - app.upery > -25:
            reset()
            return gtime

        #drawings
        #TODO make animation for the walking of the main player
        #TODO make a backround
        pygame.draw.rect(window , '#000064' , (0,0,400,400))
        pygame.draw.rect(window , '#00FFFF' , (0,350,400,400))
        #draw the charecters
        if motion == 'standing':
            window.blit(penguin, (app.p_x - 30  , app.p_y - 30))
        elif motion == 'jumping':
            window.blit(penguin_jump , (app.p_x - 30 , app.p_y - 30))
        else:
            window.blit(penguin_slide , (app.p_x - 30 , app.p_y - 20))

        window.blit (ice, (app.standerdx - 45  , app.standerdy - 35))
        window.blit(ice2 , (app.fastx - 20, app.fasty - 25))
        window.blit(ice2 , (app.flyerx - 20, app.flyery - 25))
        window.blit(ice2 , (app.diverx - 20 , app.divery - 25))
        window.blit(ice2 , (app.diverx - 20, app.divery - 25))
        window.blit(ice2 , (app.middlex - 20, app.middley - 25))
        window.blit(ice2 , (app.middlex - 20, app.middley - 25))
        window.blit(ice2 , (app.uperx - 20, app.upery - 25))

        
        

        #jump meter
        pygame.draw.rect(window , 'gray' , (0,0, 100 , 40))
        if time <= 23:
            pygame.draw.rect(window , 'red' , (5,5,5,30)) 
        if time <= 22:
            pygame.draw.rect(window, 'red' , (10,5,10,30))
        if time <= 19:
            pygame.draw.rect(window, 'red' , (15,5,15,30))
        if time <= 17:
            pygame.draw.rect(window, 'orange' , (20,5,20,30))
        if time <= 14:
            pygame.draw.rect(window, 'orange' , (25,5,25,30))
        if time <= 12:
            pygame.draw.rect(window, 'orange' , (30,5,30,30))
        if time <= 10:
            pygame.draw.rect(window, 'yellow' , (35,5,35,30))
        if time <= 8:
            pygame.draw.rect(window, 'yellow' , (40,5,40,30))
        if time <= 6:
            pygame.draw.rect(window, 'yellow' , (45,5,45,30))
        if time <= 3:
            pygame.draw.rect(window, 'green' , (50,5,40,30))
        if time <= 0:
            pygame.draw.rect(window, 'green' , (55 , 5 , 40 , 30))
        #making a score board
        font = pygame.font.SysFont('New times roman', 24)
        app.text = font.render(f'LEVEL: {level}', True, '#0000FF', '#00FFFF')
        window.blit(app.text , (300,375))
        #score
        font_2 = pygame.font.SysFont('New times roman', 24)
        app.text_2 = font_2.render(f'score: {gtime}', True, '#0000FF', '#00FFFF')
        window.blit(app.text_2 , (100,375))
        pygame.display.flip()
    pygame.quit()
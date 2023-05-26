import pygame


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
time = 0
run = True
safe = True


while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    keys = pygame.key.get_pressed()    
    app.projx -= 2

    if app.projx < 0:
        app.projx = 450
    
    if keys[pygame.K_SPACE]:
        if app.y < 50:
            pass
        elif time <= 30:
            app.y -= 4
            time += 1
            print(time)
        elif app.y < 350: 
            app.y += 2
    elif app.y < 350:
        app.y += 2
    if app.y  == 350:
        if time > 0:
            time -= 1
            print(time)
    if app.x - app.projx < 25 and app.x - app.projx > -25 and app.y - app.projy < 25 and app.y - app.projy > -25:
        break

    window.fill((0, 0, 64))
    pygame.draw.circle(window, 'green', (app.x , app.y) , 15)
    pygame.draw.circle(window, 'red' , (app.projx , app.projy) , 20)


    pygame.draw.rect(window, 'gray' , (0,365,400,400))

    #jump meater
    pygame.draw.rect(window , 'gray' , (0,0, 200 , 40))
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
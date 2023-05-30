import pygame
#pregame creation
pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
class App:
    pass
app = App()

app.x = 200
app.y = 350
run = True

while run:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    #keys means if a key is pressed
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_DOWN]:
        if app.y < 349:
            pass
        else:
            if app.y >= 360:
                app.y = 360
            app.y += 10
    elif app.y > 350:
        app.y = 350

    window.fill((0,255,0))
    pygame.draw.circle(window, 'gray' , (app.x , app.y) , 20)
    pygame.display.flip()
import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
rect = pygame.Rect(135, 220, 30, 30) 
class App:
    pass
app = App()

app.x = 50
app.y = 350
vel = 5
time = 0
run = True


def jump():
    time = 0
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()    
    
    
    if keys[pygame.K_SPACE]:
        if app.y < 50:
            pass
        elif time <= 20:
            app.y -= 10
            time += 1
            print(time)
        elif app.y < 350:
            app.y += 10
    elif app.y < 350:
        app.y += 10
    if app.y == 350:
        if time > 0:
            time -= 1
            print(time)

    window.fill((0, 0, 64))
    pygame.draw.circle(window, (255, 0, 0), (app.x,app.y), 15)
    pygame.display.flip()


while run:
    jump()

pygame.quit()
exit() 

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
app.projx = 450
app.projy = 350
time = 0
run = True

while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()    
    app.projx -= 1
    
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
    if app.y == 350:
        if time > 0:
            time -= 1
            print(time)
    
    if app.x - app.projx < 15 and app.x - app.projx > -15 and app.y - app.projy < 15 and app.y - app.projy > -15:
        break
    window.fill((0, 0, 64))
    pygame.draw.circle(window, 'green', (app.x,app.y), 15)
    pygame.draw.circle(window, 'red' , (app.projx , app.projy) , 20)
    pygame.display.flip()

pygame.quit()

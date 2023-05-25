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

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()    
    
    
    if keys[pygame.K_SPACE]:
        if app.y < 50:
            pass
        else:
            app.y -= 10
    elif app.y < 350:
        app.y += 10

    window.fill((0, 0, 64))
    pygame.draw.rect(window, (64, 64, 64), (0, 250, 300, 100))
    pygame.draw.circle(window, (255, 0, 0), (app.x,app.y), 15)
    pygame.display.flip()

pygame.quit()
exit() 
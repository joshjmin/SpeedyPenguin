import pygame
motion = 'ground'
jumping = 'standing'
class App:
    pass
app = App()
pygame.init()
pygame.display.set_caption('jumping test')
window = pygame.display.set_mode([400,400])

app.px = 50
app.py = 350

pygame.key.set_repeat(33)

def move(event):
    if event.key in [pygame.K_w]:
        while app.py > 50:
            app.py -= 0.001
            pygame.draw.circle(window ,'green' , (app.px , app.py) , 20 )
            pygame.display.flip()
        
        
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            move(event)
        
    pygame.draw.rect(window, 'gray', (0, 0, 400, 400))
    pygame.draw.circle(window ,'green' , (app.px , app.py) , 20 )
    pygame.display.flip()
pygame.quit
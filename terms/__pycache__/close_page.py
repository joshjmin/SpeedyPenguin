import pygame

def death():
    pygame.init()
    pygame.display.set_caption('Speedy Penguin DEATH')
    window = pygame.display.set_mode([400, 400])

    pygame.font.init()
    font = pygame.font.SysFont('New times roman', 35)

    death = font.render('YOU DIED', True, 'black', '#998484')
    score = font.render('Score is:', True, 'black', '#998484')
    replay= font.render('Press space to play' , True , 'black' , '#998484')

    running = False 

    while not running:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             exit()

    
    pygame.draw.rect(window, '#998484', (0, 0, 400, 400))

    window.blit(death,  (135,50) )
    window.blit(score,  (10, 150))
    window.blit(replay, (10,350))
    

    
            #quit if they press space
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        running = True

    pygame.display.flip()


    pygame.quit()

import pygame
from gameplay import gameplay
def death():
    score = gameplay()
    pygame.init()
    pygame.display.set_caption('Speedy Penguin DEATH')
    window = pygame.display.set_mode([400, 400])

    pygame.font.init()
    font = pygame.font.SysFont('New times roman', 35)

    death = font.render('YOU DIED', True, 'black', '#998484')
    score = font.render(f'Score is: {score}', True, 'black', '#998484')
<<<<<<< HEAD
    replay= font.render('Press SPACE to Play' , True , 'black' , '#998484')
    quiting = font.render('Press Q to Quit' , True , 'black' , '#998484')
=======
    replay= font.render('Press space to play again' , True , 'black' , '#998484')
    quiting = font.render('Press Q to quit' , True , 'black' , '#998484')
>>>>>>> cf719d286f180ee81d3cb8fdf0af220321e916f6

    running = False 

    while not running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    
        pygame.draw.rect(window, '#998484', (0, 0, 400, 400))

        window.blit(death,  (135,50) )
        window.blit(score,  (10, 150))
        window.blit(replay, (10,350))
        window.blit(quiting , (10 , 250))
    
        dead = pygame.image.load('src/assets/dizzy_penguin.png')
        dead = pygame.transform.scale(dead , (150,130))
        window.blit(dead , (200 , 200))
    
            #quit if they press space
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            running = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            exit()

        pygame.display.flip()


    pygame.quit()

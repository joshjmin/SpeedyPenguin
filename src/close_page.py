import pygame
from gameplay import gameplay


def death() -> None:

    #Sets up the score function 
    score = gameplay()

    #Creates window 
    pygame.init()
    pygame.display.set_caption('Speedy Penguin DEATH')
    window = pygame.display.set_mode([400, 400])

    #Define text size and font type 
    pygame.font.init()
    font = pygame.font.SysFont('New times roman', 35)

    #Draw text 
    death = font.render('YOU DIED', True, 'black', '#998484')
    score = font.render(f'Score is: {score}', True, 'black', '#998484')
    replay= font.render('Press SPACE to Play' , True , 'black' , '#998484')
    quiting = font.render('Press Q to Quit' , True , 'black' , '#998484')

    """
    Set up a window with the text displaying a GAME OVER message 
    and the score of that round.
    Player is then presented with the choice of either 
    playing again by pressing space or quiting the game 
    by pressing q. Space will then take the player back to the options screen. 
    Q will close the game. 
    It also have a dizzy penguin image located on the right.
    
    """


    running = False 

    #Main Loop 
    while not running:

        #Check if quit then quit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    
        pygame.draw.rect(window, '#998484', (0, 0, 400, 400))

        #Place text on window using graph points 
        window.blit(death,  (135,50) )
        window.blit(score,  (10, 150))
        window.blit(replay, (10,350))
        window.blit(quiting , (10 , 250))
    
        #Open dizzy penguin 
        dead = pygame.image.load('src/assets/dizzy_penguin.png')
        dead = pygame.transform.scale(dead , (150,130))
        window.blit(dead, (200 , 200))
    
        #resume game if space is pressed 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            running = True
            
        #quit game if q is pressed 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            exit()

        pygame.display.flip()


    pygame.quit()

import pygame

class App:
    pass
app = App()
clock = pygame.time.Clock()
def title_text() -> None:

    # Set up the window
    pygame.init()
    pygame.display.set_caption('Speedy Penguin')
    window = pygame.display.set_mode([360, 330])

    # Set up text module
    pygame.font.init()
    font = pygame.font.SysFont('New times roman', 30)

    # Define text
    text = font.render('WELCOME TO SPEEDY PENGUIN', True, 'black', '#A5F2F3')
    text_2 = font.render('PRESS SPACE TO CONTINUE', True, 'black', '#A5F2F3')
        
    """
    
    Sets up an opening window that displays 
    an opening message and
    sets to continue to the next page. 
    It also displays a cute image 
    of a penguin that is used in the game. 
    
    """


    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # Draw shapes
        pygame.draw.rect(window, '#A5F2F3', (0, 0, 400, 400))

        # Draw text
        window.blit(text, (20, 50))
        window.blit(text_2, (20, 100))


        #make the main character
        pen = pygame.image.load('src/assets/penguin_standing.png')
        pen = pygame.transform.scale(pen, (80,120))
        window.blit(pen, (120, 180))

        #quit if they press space
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:

            running = False

        # Update the display
        pygame.display.flip()

    # Quit the window
    pygame.quit()
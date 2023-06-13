class App:
    pass
app = App()
import pygame
def difficulty() -> int:

# Set up the window
    pygame.init()
    pygame.display.set_caption('Speedy Penguin')
    window = pygame.display.set_mode([400, 400])

# Set up text module
    pygame.font.init()
    font = pygame.font.SysFont('New times roman', 25)

# Define text
    text = font.render('CHOOSE THE DIFFICULTY:', True, 'black', '#A5F2F3')
    text_2 = font.render('EASY = 1' , True , 'black' , '#A5F2F3')
    text_3 = font.render('NORMAL = 2', True, 'black', '#A5F2F3')
    text_4 = font.render('HARD = 3', True, 'black', '#A5F2F3')

    """

    This screen appears after the 2 opening screens and offer 
    the user the choice of chosing between 3 different modes 
    or levels ranging from easy to hard. The speed and jump
    are the only controls that change as a result of this choice.

    """

# Main loop
    running = True
    app.penx = -100
    app.peny = 300
    while running:
        app.penx += 5
        if app.penx >= 1000:
            app.penx = -100
    # Check events
        for event in pygame.event.get():
        # User clicks window close button
            if event.type == pygame.QUIT:
                exit()

    # Draw shapes
        pygame.draw.rect(window, '#A5F2F3', (0, 0, 400, 400))

    # Draw text
        window.blit(text, (10, 60))
        window.blit(text_2 , (10,120))
        window.blit(text_3, (10, 160))
        window.blit(text_4, (10, 200))

    #make the main charecter
        pen = pygame.image.load('src/assets/penguin_sliding(pink).png')
        pen = pygame.transform.scale(pen, (120,100))
        window.blit(pen, (app.penx,app.peny))

        #quit if they press space
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            return 1
        if keys[pygame.K_2]:
            return 0
        if keys[pygame.K_3]:
            return -3
    # Update the display
        pygame.display.flip()
    pygame.quit()
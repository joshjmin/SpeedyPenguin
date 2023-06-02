import pygame
class App:
    pass
app = App()

def open_text():

# Set up the window
    pygame.init()
    pygame.display.set_caption('Speedy Penguin')
    window = pygame.display.set_mode([400, 400])

# Set up text module
    pygame.font.init()
    font = pygame.font.SysFont('New times roman', 25)

# Define text
    text = font.render('PRESS W/UP to Jump', True, 'black', '#A5F2F3')
    text_2 = font.render('PRESS S/DOWN to Slide', True, 'black', '#A5F2F3')
    text_3 = font.render('Press SPACE to Play' , True , 'black', '#A5F2F3')
# Main loop
    running = True
    while running:

    # Check events
        for event in pygame.event.get():
        # User clicks window close button
            if event.type == pygame.QUIT:
                exit()

    # Draw shapes
        pygame.draw.rect(window, '#A5F2F3', (0, 0, 400, 400))

    # Draw text
        window.blit(text, (10, 50))
        window.blit(text_2, (10, 90))
        window.blit(text_3, (10,160))

    #make the main charecter
        pen = pygame.image.load('src/assets/penguin<3.png')
        pen = pygame.transform.scale(pen, (150,150))
        window.blit(pen, (150,150))

        #quit if they press space
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            running = False

    # Update the display
        pygame.display.flip()

# Quit the window
    pygame.quit()
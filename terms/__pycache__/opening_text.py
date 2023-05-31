import pygame
class App:
    pass
app = App()

def open_text():

# Set up the window
    pygame.init()
    pygame.display.set_caption('My very first pygame GUI')
    window = pygame.display.set_mode([300, 300])

# Set up text module
    pygame.font.init()
    font = pygame.font.SysFont('New times roman', 16)

# Define text
    text = font.render('W/UP;Jump and S/DOWN; slide', True, 'black', '#A5F2F3')
    text_2 = font.render('Press space to play' , True , 'black' , '#A5F2F3')
# Main loop
    running = True
    while running:

    # Check events
        for event in pygame.event.get():
        # User clicks window close button
            if event.type == pygame.QUIT:
                exit()

    # Draw shapes
        pygame.draw.rect(window, '#A5F2F3', (0, 0, 300, 300))

    # Draw text
        window.blit(text, (10, 100))
        window.blit(text_2 , (10,150))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            running = False

    # Update the display
        pygame.display.flip()

# Quit the window
    pygame.quit()


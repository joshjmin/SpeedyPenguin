import pygame
class App:
    pass
app = App()

def open_text():

# Set up text module
    pygame.font.init()
    font = pygame.font.SysFont('New times roman', 30)

# Define text
    text = font.render('PRESS W/UP to Jump', True, 'black', '#A5F2F3')
    text_2 = font.render('PRESS S/DOWN to Slide', True, 'black', '#A5F2F3')
    text_3 = font.render('PRESS SPACE to Play' , True , 'black' , '#A5F2F3')
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
        window.blit(text, (20, 60))
        window.blit(text_2, (20, 100))
        window.blit(text_3 , (20,200))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            running = False

    # Update the display
        pygame.display.flip()

# Quit the window
    pygame.quit()




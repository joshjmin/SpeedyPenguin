import pygame

class App:
    pass
app = App()
clock = pygame.time.Clock()
def open_text() -> None:

# Set up the window
    pygame.init()
    pygame.display.set_caption('Speedy Penguin')
    window = pygame.display.set_mode([300, 330])

# Set up text module
    pygame.font.init()
    font = pygame.font.SysFont('New times roman', 25)

# Define text
    text = font.render('PRESS W/UP to Jump', True, 'black', '#A5F2F3')
    text_2 = font.render('PRESS S/DOWN to Slide', True, 'black', '#A5F2F3')
    text_3 = font.render('Press SPACE to Play' , True , 'black', '#A5F2F3')


    """

    Set up a window with the text displaying a start game message.
    The screen gives instructions to the player as to how to 
    play (w/up to jump, s/down to slide and space to jump).
    The screen also has a moving penguin in the 
    flying motion used for the game its self 
    
    """
# Main loop
    running = True
    frame = 1
    going = 'up'
    while running:
        clock.tick(120)
        if frame < 0:
            frame += 0.3
            going = 'up'
        if frame > 50:
            frame -= 0.3
            going = 'down'

        if going == 'up':
            frame += 0.3
        elif going == 'down':
            frame -= 0.3
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
        pen = pygame.image.load('src/assets/flyingpenguin(pink).png')
        pen = pygame.transform.scale(pen, (120,100))
        window.blit(pen, (50 + frame , 170 + frame))

        #quit if they press space
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            running = False

    # Update the display
        pygame.display.flip()

# Quit the window
    pygame.quit()

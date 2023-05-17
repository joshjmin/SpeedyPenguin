import pygame

# Set up the window
pygame.init()
pygame.display.set_caption('My very first pygame GUI')
window = pygame.display.set_mode([400, 400])

# Set up text module
pygame.font.init()
font = pygame.font.SysFont('Courier New', 24)

# Main loop
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw shapes
    pygame.draw.rect(window, 'red', (0, 0, 200, 200))
    pygame.draw.rect(window, 'green', (200, 0, 400, 200))
    pygame.draw.rect(window, 'yellow', (200, 200, 400, 400))
    pygame.draw.rect(window, 'blue', (0, 200, 200, 400))

    # Draw text
    text = font.render('Windows 95', True, 'white', 'black')
    window.blit(text, (130, 185))

    # Update the display
    pygame.display.flip()

# Quit the window
pygame.quit()

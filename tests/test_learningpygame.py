import pygame
import random
from time import sleep
# Create an app object to store global variables
class App:
    pass
app = App()
# Set up the window
pygame.init()
pygame.display.set_caption('Collect all the coins')
window = pygame.display.set_mode([400, 400])


# Initialize app variables
x = 10_000
coins = 0
app.player_x = 200
app.player_y = 200
app.cpu_x = 0
app.cpu_y = 0
app.cpu_x_2 = -100
app.cpu_y_2 = -100
app.cpu_x_3 = 450
app.cpu_y_3 = 450
app.coin_x = random.randint(50,50)
app.coin_y = random.randint(50,50)
time = 0
freeze = 'off'

# Allow repeated keypressing every N milliseconds
pygame.key.set_repeat(33)

# Functions

def move(event) -> None:
    """
    Move the player using WASD or arrow keys.
    """

    if event.key in [pygame.K_w, pygame.K_UP]:
        if app.player_y > 25:
            app.player_y -= (10 + user_speed_scaling)

    elif event.key in [pygame.K_s, pygame.K_DOWN]:
        if app.player_y < 375:
            app.player_y += (10 + user_speed_scaling)

    elif event.key in [pygame.K_a, pygame.K_LEFT]:
        if app.player_x > 25:
            app.player_x -= (10 + user_speed_scaling)

    elif event.key in [pygame.K_d, pygame.K_RIGHT]:
        if app.player_x < 375:
            app.player_x += (10 + user_speed_scaling)



def cpu_1_movment():
    if app.cpu_x > app.player_x:
        app.cpu_x -= (1 + user_speed_scaling)
    elif app.cpu_x < app.player_x:
        app.cpu_x += (1 + user_speed_scaling)
    if app.cpu_y > app.player_y:
        app.cpu_y -= (1 + user_speed_scaling)
    elif app.cpu_y < app.player_y:
        app.cpu_y += (1 + user_speed_scaling)
def cpu_2_movment():
    if app.cpu_x_2 > app.player_x:
        app.cpu_x_2 -= (1.5 + speed_scaling)
    elif app.cpu_x_2 < app.player_x:
        app.cpu_x_2 += (1.5 + speed_scaling)
    if app.cpu_y_2 > app.player_y:
        app.cpu_y_2 -= (1.5 + speed_scaling)
    elif app.cpu_y_2 < app.player_y:
        app.cpu_y_2 += (1.5 + speed_scaling)
def cpu_3_movment():
    if app.cpu_x_3 > app.player_x:
        app.cpu_x_3 -= (2 + speed_scaling)
    elif app.cpu_x_3 < app.player_x:
        app.cpu_x_3 += (2 + speed_scaling)
    if app.cpu_y_3 > app.player_y:
        app.cpu_y_3 -= (2 + speed_scaling)
    elif app.cpu_y_3 < app.player_y:
        app.cpu_y_3 += (2 + speed_scaling)

 
# Main loop
time = 0
running = True
while running:
    time += 1
    if time > 10:
        cpu_1_movment()
    if time > 1000:
        cpu_2_movment()
    if time > 2000:
        cpu_3_movment()


    #setting the speed and acceleration
    speed_scaling = (time * 0.0001)
    user_speed_scaling = (time * 0.0001 + (0.015 * coins))


    # Catch all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and freeze == 'off':
            move(event)

    # Draw the background

    pygame.draw.rect(window, 'gray', (0, 0, 400, 400))

        #making the score counter

    pygame.font.init()
    font = pygame.font.SysFont('New Times Roman', 24)
    app.text = font.render(f'{coins}' , True , 'black' , 'gray')
    window.blit(app.text , (200,180))

    #making the speed buff counter
    pygame.font.init()
    app.score = font.render(f'speed; {user_speed_scaling * 10}' , True , 'black' , 'gray')
    if speed_scaling > 0:
        window.blit(app.score , (300,350))

    #making the score board on top
    pygame.font.init()
    app.toatl = font.render(f'score; {time}' , True , 'black' , 'gray')
    window.blit(app.toatl , (10,10))

    # Draw the player
    pygame.draw.circle(window, 'green', (app.player_x, app.player_y), 20)
    pygame.draw.circle(window, 'purple',(app.cpu_x , app.cpu_y) , 20)
    pygame.draw.circle(window,'blue' , (app.cpu_x_2 , app.cpu_y_2) , 20)
    pygame.draw.circle(window, 'red' , (app.cpu_x_3 , app.cpu_y_3) , 20)
    pygame.draw.circle(window , 'yellow' , (app.coin_x , app.coin_y) , 10)

#coin collection
    if app.player_x - app.coin_x < 20 and app.player_y - app.coin_y < 20 and app.player_x - app.coin_x > -20 and app.player_y - app.coin_y > -20:
        app.coin_x = random.randint(150,350)
        app.coin_y = random.randint(150,350)
        coins += 1
        time += 150


#if you get hit this is a full restart

    if app.player_x - app.cpu_x_2 < 30 and app.player_y - app.cpu_y_2 < 30 and app.player_x - app.cpu_x_2 > -30 and app.player_y - app.cpu_y_2 > -30:
        freeze = 'on'
        sleep(1)
        coins = 0
        app.player_x = 200
        app.player_y = 200
        app.cpu_x = 0
        app.cpu_y = 0
        app.cpu_x_2 = -100
        app.cpu_y_2 = -100
        app.cpu_x_3 = 450
        app.cpu_y_3 = 450
        app.coin_x = random.randint(50,50)
        app.coin_y = random.randint(50,50)
        time = 0
        for i in range(x):
            freeze = 'off'
            app.player_x = 200
            app.player_y = 200
    if app.player_x - app.cpu_x_3 < 30 and app.player_y - app.cpu_y_3 < 30 and app.player_x - app.cpu_x_3 > -30 and app.player_y - app.cpu_y_3 > -30:
        freeze = 'on'
        sleep(1)
        coins = 0
        app.player_x = 200
        app.player_y = 200
        app.cpu_x = 0
        app.cpu_y = 0
        app.cpu_x_2 = -100
        app.cpu_y_2 = -100
        app.cpu_x_3 = 450
        app.cpu_y_3 = 450
        app.coin_x = random.randint(50,50)
        app.coin_y = random.randint(50,50)
        time = 0
        for i in range(x):
            freeze = 'off'
    if app.player_x - app.cpu_x < 30 and app.player_y - app.cpu_y < 30 and app.player_x - app.cpu_x > -30 and app.player_y - app.cpu_y > -30:
        freeze = 'on'
        sleep(1)
        coins = 0
        app.player_x = 200
        app.player_y = 200
        app.cpu_x = 0
        app.cpu_y = 0
        app.cpu_x_2 = -100
        app.cpu_y_2 = -100
        app.cpu_x_3 = 450
        app.cpu_y_3 = 450
        app.coin_x = random.randint(50,50)
        app.coin_y = random.randint(50,50)
        time = 0
        for i in range(x):
            freeze = 'off'
    # Update the display
    pygame.display.flip()
# Quit the window
pygame.quit()
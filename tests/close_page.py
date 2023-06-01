import pygame

pygame.init()
pygame.display.set_caption('Speedy Penguin DEATH')
window = pygame.display.set_mode([300, 300])

pygame.font.init()
font = pygame.font.SysFont('New times roman', 24)

score = font.render('Score is:', True, 'black', '#c91818')
replay= font.render('Press space to play' , True , 'black' , '#c91818')
death = font.render('YOU DIED', True, 'black', '#c91818')

running = False

while not running:


   for event in pygame.event.get():
      if event.type == pygame.QUIT:
          exit()

   
   pygame.draw.rect(window, '#c91818', (0, 0, 300, 300))

   window.blit(score, (10, 100))
   window.blit(replay , (10,250))
   window.blit(death, (100,50) )

   
        #quit if they press space
   keys = pygame.key.get_pressed()
   if keys[pygame.K_SPACE]:
       running = False

   pygame.display.flip()


pygame.quit()

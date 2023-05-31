import pygame
import sys


pygame.init()
running = True 
width= 400 
height = 400 
window = pygame.display.set_mode((width, height))


def death():
   
   window.fill((255, 255, 255))

   font = pygame.font.SysFont('Times New Roman', 34)

   death_text = font.render('Game Over', True, (0, 0, 0))

   replay = font.render('Press space to replay ', True, (0, 0, 0)
                        )
   quit_button = font.render('Press x to quit', True, (0, 0, 0))

   window.blit(death_text, (width/2 - death_text.get_width()/2, height/2 - death_text.get_height()/3))

   window.blit(replay, (width/2 - replay.get_width()/2, height/1.9 + replay.get_height()))

   window.blit(quit_button, (width/2 - quit_button.get_width()/2, height/2 + quit_button.get_height()/2))

   pygame.display.update()

   pygame.display.flip()

while running:
   for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        pygame.draw.rect(death)
    
pygame.quit()
   
              

   
       
           
      
  



  





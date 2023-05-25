
import os
import sys
import pygame
import random
from pygame import *

pygame.init()

screenDisplay = (width_screen, height_screen) = (600, 400)
FPS = 60
gravity = 0.6

black_color = (0,0,0)
white_color = (255,255,255)
backgroundColor = (235, 235, 235)

highest_scores = 0

screenDisplay = pygame.display.set_mode(screenDisplay)
timerClock = pygame.time.Clock()
pygame.display.set_caption("Dino Run - CopyAssignment ")


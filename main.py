# importo pygame for grafics, random for numbers and sys to close the program properly
import tkinter as tk
import pygame, random, sys
from pygame.locals import *
# importo subfunctions from pygame
##from pygame.locals import *
# despues necesitamos inicialicar nuestro pygame
pygame.init()
# ahora configurarmos el tamaño de nuestra ventana y le ponemos titulo
# res rec 960x720
screen = pygame.display.set_mode((960,720))
pygame.display.set_caption('Balloon Pop')
#Ahora podemos importar nuestro bg, y sacar de la imagen el rectangulo rectangulo
background = pygame.image.load('gingerbread.png')
bg_rect = background.get_rect()
bg_rect.left = 0
bg_rect.top = 0
test = screen.get_width()
#Goblo
balloon = pygame.image.load('balloon.png')
balloon_rect = balloon.get_rect()
balloon_rect.left = balloon_rect.width + (random.random() *(screen.get_width() - balloon_rect.width *2)) # lo separamos de la izquierda su tamaño generemos aleatorio y lo multiplicamos por el ancho de la pantalla menos el ancho del rectangulo * 2 para que aparezca solo por en medio

# AHORA LA PARTE SUPERIOR DEL BALLOON
balloon_rect.top = screen.get_height() - balloon_rect.height / 2
# y le ponemos una velocidad de agetreo
drift = 2
#Creamos un relog para controlar la velocidad del juego
clock = pygame.time.Clock()

# Ahora enviamos el bg a la ventana
# le tenemos que pasar tanto la imagen como el rectangulo.
screen.blit(background, bg_rect)
screen.blit(balloon, balloon_rect)

#Al final tenemos que actualizar la ventana  para asegurarnos que nuestra imagen se ve bien.
# esto tiene que ir siempre al final de codigo


while True:
  balloon_rect.top -= 2
  balloon_rect.left += drift
  # controles de posicion del glovo
  if balloon_rect.top < 2: # si llega arriba lo bajamos
    balloon_rect.top = screen.get_height() - balloon_rect.height / 2
  elif balloon_rect.left < 2 or balloon_rect.left > screen.get_width() - balloon_rect.width - 2:
    drift *= -1
  screen.blit(background, bg_rect)
  screen.blit(balloon, balloon_rect)
  pygame.display.update()
  clock.tick(60) #slow the fps

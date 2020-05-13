# importo pygame for grafics, random for numbers and sys to close the program properly
import tkinter as tk
import pygame, random, sys
from pygame.locals import *

class Balloon():
  def __init__(self):
  #Goblo
    self.balloon = pygame.image.load('balloon.png')
    self.balloon_rect = self.balloon.get_rect()
    self.balloon_rect.left = self.balloon_rect.width + (random.random() *(screen.get_width() - 
    self.balloon_rect.width *2)) 
    self.balloon_rect.top = screen.get_height() - self.balloon_rect.height / 2
    # lo separamos de la izquierda su tamaño generemos aleatorio y lo multiplicamos por el ancho de la pantalla menos el ancho del rectangulo * 2 para que aparezca solo por en medio
    if random.random() > 0.5: # direccion aleatiorio en Y
      self.drift = 2
    else:
      self.drift = -2
  def update(self):
    self.balloon_rect.top -= 2
    self.balloon_rect.left += self.drift
    # controles de posicion del glovo
    if self.balloon_rect.top < 2: # si llega arriba lo bajamos
      self.balloon_rect.top = screen.get_height() - self.balloon_rect.height / 2
    elif self.balloon_rect.left < 2 or self.balloon_rect.left > screen.get_width() - self.balloon_rect.width - 2:
      self.drift *= -1
    screen.blit(self.balloon, self.balloon_rect)
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

# y le ponemos una velocidad de agetreo
#Creamos un relog para controlar la velocidad del juego
clock = pygame.time.Clock()

# Ahora enviamos el bg a la ventana
# le tenemos que pasar tanto la imagen como el rectangulo.
#screen.blit(background, bg_rect)

# Creamos un array apra almacenar todos nuestros objetos ballon
balloons = []
# loop te mañano 10 para generar 10 balloons y los agregamos al array
for x in range(10):
  balloons.append(Balloon())

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit
      raise SystemExit
    elif event.type == pygame.MOUSEBUTTONDOWN:
      x, y = event.pos
      if balloon_rect.collidepoint(x, y):
        balloon_rect.left = balloon_rect.width + (random.random() *(screen.get_width() - balloon_rect.width *2))
        balloon_rect.top = screen.get_height() - balloon_rect.height / 2
          
  screen.blit(background, bg_rect)
  for Balloon in balloons:
    Balloon.update()
  pygame.display.update()
  clock.tick(60) #slow the fps

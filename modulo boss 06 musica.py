import pygame
import time

# Inicializar o pygame
pygame.init()

# Carregar a música
pygame.mixer.music.load('ex21.mp3')

# Tocar a música
pygame.mixer.music.play()

# Esperar enquanto a música toca
while pygame.mixer.music.get_busy():
    time.sleep(1)

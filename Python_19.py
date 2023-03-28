import emoji
import pygame
n = input(emoji.emojize('Aperte ENTER para escutar :guitar::metal:', language='alias'))
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ACDC.mp3')
pygame.mixer.music.play()
input()

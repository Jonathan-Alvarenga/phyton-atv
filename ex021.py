#Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer_music.load('ex021.mp3')
pygame.mixer_music.play()
input()
pygame.event.wait()

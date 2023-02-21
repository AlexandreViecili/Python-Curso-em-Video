# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.mixer.init()
pygame.mixer.music.load('doom.mp3')
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play()
input()
import pygame


def play_songs():
    clock = pygame.time.Clock()
    pygame.mixer.init()
    pygame.mixer.music.load("audio/Planet-Claire.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        clock.tick(30)

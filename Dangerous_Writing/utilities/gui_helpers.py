import sys

import pygame

import os

# just used to make .exe file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def play_sound():
    try:
        sound_file = "Dangerous_Writing/resources/Tick.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
    except pygame.error:
        pass






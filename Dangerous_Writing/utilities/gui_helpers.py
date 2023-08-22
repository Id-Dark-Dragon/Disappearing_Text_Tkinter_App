import pygame

def play_sound():
    try:
        sound_file = "Dangerous_Writing/resource/Tick.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
    except pygame.error:
        pass






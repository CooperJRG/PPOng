import pygame
from src.menu import Menu
from src.game import Game
from src.options import Options
from src.stats import Stats


def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((640, 480))  # example resolution
    pygame.display.set_caption("PPOng")

    # States
    self.states = {
        "MENU": Menu(self.screen),
        "GAME": Game(self.screen),
        "OPTIONS": Options(self.screen),
        "STATS": Stats(self.screen)
    }
    self.current_state = self.states["MENU"]

# Author: Colin Francis
# Description: An implementation of Langton's Ant using Pygame

import pygame
from settings import *


class LangtonsAnt(object):
    def __init__(self):
        self._running = True
        self._board = Board()

    def start(self):
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
            pygame.display.update()


class Board(object):
    def __init__(self):
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._screen.fill(WHITE)
        pygame.display.set_caption("Langton's Ant")


if __name__ == "__main__":
    langtons_ant = LangtonsAnt()
    langtons_ant.start()

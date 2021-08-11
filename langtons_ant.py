# Author: Colin Francis
# Description: An implementation of Langton's Ant using Pygame

import pygame
from settings import *


class LangtonsAnt(object):
    """A class used to visualize Langton's Ant - a two-dimensional universal Turing
    machine with a simple set of rules but complex emergent behavior. Rules:
        1.) At a white square, turn 90 degrees clockwise, turn the color of the square
            black and move forward one unit.
        2.) At a black square, turn 90 degrees counter-clockwise, turn the color of
            the square white, move forward one unit.
    """
    def __init__(self) -> None:
        """Creates a LangtonsAnt object."""
        self._running = True
        self._board = Board()
        self._states = self._init_states()

    def start(self):
        """Begins running Langton's Ant according to the established rules."""
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
            self._board.update()
            pygame.display.update()

    def _init_states(self) -> dict:
        pass


class Board(object):
    """Represents a Board with a square lattice of black and white cells used for running
    Langton's Ant."""
    def __init__(self) -> None:
        """Creates a Board object"""
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._screen.fill(WHITE)
        pygame.display.set_caption("Langton's Ant")

    def update(self) -> None:
        """Updates the state of the Board."""
        self._draw_grid()

    def _draw_grid(self) -> None:
        """Draws the square grid used in Langton's Ant."""
        # draw the grid boarder
        pygame.draw.rect(self._screen,
                         BLACK,
                         pygame.Rect(GRID_LEFT, GRID_TOP, GRID_WIDTH - 1, GRID_HEIGHT - 1),
                         width=2
                         )

        # draw grid lines
        for coord in range(SQUARE_WIDTH, GRID_WIDTH, SQUARE_WIDTH):
            # vertical grid lines
            pygame.draw.line(self._screen, BLACK,
                             (coord, GRID_TOP),
                             (coord, GRID_HEIGHT),
                             width=2
                             )

            # horizontal grid lines
            pygame.draw.line(self._screen,
                             BLACK,
                             (GRID_LEFT, coord),
                             (GRID_WIDTH, coord),
                             width=2)


# General Testing and Verification - Driver Code:
if __name__ == "__main__":
    langtons_ant = LangtonsAnt()
    langtons_ant.start()

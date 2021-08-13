# Author: Colin Francis
# Description: An implementation of Langton's Ant using Pygame

import pygame
from settings import *


class LangtonsAnt(object):
    """A class used to run a visual simulation of Langton's Ant."""
    def __init__(self):
        """Creates a LangtonsAnt object."""
        self._running = True
        self._board = Board()
        self._ant = Ant(self._board)

    def start(self):
        """Runs LangtonsAnt up to 10,500 iterations."""
        while self._running:  # main simulation loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
            self._board.update()  # update the state of the Board
            pygame.display.update()  # update the display


class Board(object):
    """Represents a Board for Langton's Ant to move in."""
    def __init__(self):
        """Creates a Board object."""
        self._board = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._board.fill(WHITE)
        pygame.display.set_caption("Langton's Ant")
        self._square_colors = self._init_square_colors()

    def update(self):
        """Updates the state of the Board."""
        self._draw_grid()

    def get_board(self):
        """Returns the Pygame Surface used as the Board."""
        return self._board

    def get_square_colors(self):
        """Returns the dictionary that contains the color of each square on
        the Board"""
        return self._square_colors

    def _draw_grid(self):
        """Draws the grid on the Board that the Ant will walk in."""
        # draw grid outline
        pygame.draw.rect(self._board,
                         BLACK,
                         pygame.Rect(GRID_LEFT,
                                     GRID_TOP,
                                     GRID_WIDTH - 1,
                                     GRID_HEIGHT
                                     ),
                         width=2
                         )

        # draw grid lines
        for coord in range(SQUARE_WIDTH, GRID_WIDTH, SQUARE_WIDTH):
            # vertical grid lines
            pygame.draw.line(self._board,
                             BLACK,
                             (coord, GRID_TOP),
                             (coord, GRID_HEIGHT),
                             width=1
                             )
            # horizontal grid lines
            pygame.draw.line(self._board, BLACK,
                             (GRID_LEFT, coord),
                             (GRID_WIDTH, coord),
                             width=1
                             )

    @staticmethod
    def _init_square_colors() -> dict:
        """Initializes a dictionary containing the color of each square on the
        Board."""
        square_colors = {}
        for row in range(ROWS):
            for col in range(COLS):
                square_colors[(row, col)] = WHITE
        return square_colors


class Ant(object):
    """Represents an Ant that moves according to the rules of Langton's Ant."""
    def __init__(self, board: Board):
        """Creates an Ant object."""
        self._position = (4, 4)
        self._board = board

    def move(self):
        pass


# General Testing and Drive Code:
if __name__ == '__main__':
    langtons_ant = LangtonsAnt()
    langtons_ant.start()

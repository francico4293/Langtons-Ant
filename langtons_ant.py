# Author: Colin Francis
# Description: An implementation of Langton's Ant using Pygame

import pygame
import time
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
        self._prev_pos = None
        self._curr_pos = (4, 4)
        self._board = Board()
        self._ant = Ant(self._board)
        self._states = self._init_states()
        self._heading = 'N'

    def start(self):
        """Begins running Langton's Ant according to the established rules."""
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
            self._prev_pos = self._curr_pos
            self._curr_pos = self._update_pos()
            self._board.update(self._prev_pos, self._states)
            self._ant.update(self._curr_pos)
            pygame.display.update()
            time.sleep(0.5)

    @staticmethod
    def _init_states() -> dict:
        states = {}
        for row in range(10):
            for col in range(10):
                if row == 4 and col == 4:
                    states[(row, col)] = {'color': WHITE}
                else:
                    states[(row, col)] = {'color': WHITE}
        return states

    def _update_pos(self):
        if self._heading == 'N':
            if self._states[self._curr_pos]['color'] == WHITE:
                self._heading = 'E'
                return self._curr_pos[0] + 1, self._curr_pos[1]
            else:
                self._heading = 'W'
                return self._curr_pos[0] - 1, self._curr_pos[1]
        elif self._heading == 'E':
            if self._states[self._curr_pos]['color'] == WHITE:
                self._heading = 'S'
                return self._curr_pos[0], self._curr_pos[1] + 1
            else:
                self._heading = 'N'
                return self._curr_pos[0], self._curr_pos[1] - 1
        elif self._heading == 'S':
            if self._states[self._curr_pos]['color'] == WHITE:
                self._heading = 'W'
                return self._curr_pos[0] - 1, self._curr_pos[1]
            else:
                self._heading = 'E'
                return self._curr_pos[0] + 1, self._curr_pos[1]
        else:
            if self._states[self._curr_pos]['color'] == WHITE:
                self._heading = 'N'
                return self._curr_pos[0], self._curr_pos[1] - 1
            else:
                self._heading = 'S'
                return self._curr_pos[0], self._curr_pos[1] + 1


class Board(object):
    """Represents a Board with a square lattice of black and white cells used for running
    Langton's Ant."""
    def __init__(self) -> None:
        """Creates a Board object"""
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._screen.fill(WHITE)
        pygame.display.set_caption("Langton's Ant")

    def update(self, position, states) -> None:
        """Updates the state of the Board."""
        self._color_square(position, states)
        self._draw_grid()

    def get_screen(self):
        return self._screen

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

    def _color_square(self, position: tuple, states: dict):
        if states[position]['color'] == WHITE:
            states[position]['color'] = BLACK
            pygame.draw.rect(self._screen, BLACK,
                             pygame.Rect(position[0] * SQUARE_WIDTH,
                                         position[1] * SQUARE_WIDTH,
                                         SQUARE_WIDTH, SQUARE_WIDTH
                                         )
                             )
        else:
            states[position]['color'] = WHITE
            pygame.draw.rect(self._screen, WHITE,
                             pygame.Rect(position[0] * SQUARE_WIDTH,
                                         position[1] * SQUARE_WIDTH,
                                         SQUARE_WIDTH, SQUARE_WIDTH
                                         )
                             )


class Ant(object):
    def __init__(self, board: Board):
        self._board = board

    def update(self, position):
        pygame.draw.circle(self._board.get_screen(), RED, (position[0] * SQUARE_WIDTH + (SQUARE_WIDTH / 2),
                                                           position[1] * SQUARE_WIDTH + (SQUARE_WIDTH / 2)), 10)


# General Testing and Verification - Driver Code:
if __name__ == "__main__":
    langtons_ant = LangtonsAnt()
    langtons_ant.start()

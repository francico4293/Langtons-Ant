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
        self._iteration = 0
        pygame.font.init()

    def start(self) -> None:
        """Runs LangtonsAnt simulation."""
        while self._running:  # main simulation loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
            if self._ant.get_position()[0] >= 0:
                self._ant.update()  # update the position of the Ant
                self._board.update()  # update the state of the Board
                self.display_iterations()  # show the current iteration count
                self._iteration += 1  # increment iteration count
            pygame.display.update()  # update the display

    def display_iterations(self):
        """Displays the current iteration number."""
        # create a surface to overwrite current iteration with
        iter_surface = pygame.Surface((GRID_WIDTH, SCREEN_HEIGHT - GRID_HEIGHT))
        iter_surface.fill(WHITE)
        self._board.get_board().blit(iter_surface, (GRID_LEFT, GRID_HEIGHT + 2))

        # display the current iteration number
        font = pygame.font.SysFont('Times New Roman', 30)
        iterations = font.render('Iteration: {}'.format(self._iteration), False, BLACK)
        self._board.get_board().blit(iterations, (0, SCREEN_HEIGHT - 45))


class Board(object):
    """Represents a Board for Langton's Ant to move in."""
    def __init__(self):
        """Creates a Board object."""
        self._board = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._board.fill(WHITE)
        pygame.display.set_caption("Langton's Ant")
        self._square_colors = self._init_square_colors()

    def update(self) -> None:
        """Updates the state of the Board."""
        self._draw_grid()

    def get_board(self) -> any:
        """Returns the Pygame Surface used as the Board."""
        return self._board

    def get_square_colors(self) -> dict:
        """Returns the dictionary that contains the color of each square on
        the Board"""
        return self._square_colors

    def flip_color(self, position: tuple, color: tuple) -> None:
        """Flips the color of the current square - if the color of the square is
        white, it will be colored black, otherwise if the color of the square is
        black, it will be colored white."""
        pygame.draw.rect(self._board,
                         color,
                         pygame.Rect(
                             position[0] * SQUARE_WIDTH,
                             position[1] * SQUARE_HEIGHT,
                             SQUARE_WIDTH, SQUARE_HEIGHT)
                         )

    def _draw_grid(self) -> None:
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
        self._position = (40, 40)
        self._heading = 'N'
        self._board = board

    def update(self) -> None:
        """Updates the position of the Ant on the Board."""
        # move the Ant
        self._move()

        # update the position of the Ant
        pygame.draw.circle(self._board.get_board(),
                           RED,
                           ((self._position[0] * SQUARE_WIDTH) + (SQUARE_WIDTH / 2),
                            self._position[1] * SQUARE_HEIGHT + (SQUARE_HEIGHT / 2)),
                           2
                           )

    def get_position(self) -> tuple:
        """Returns the current position of the Ant."""
        return self._position

    def _move(self) -> None:
        """Moves the Ant based on the movement rules of Langton's Ant."""
        square_colors = self._board.get_square_colors()

        if self._heading == 'N':
            if square_colors[self._position] == WHITE:
                square_colors[self._position] = BLACK
                self._board.flip_color(self._position, BLACK)
                self._position = (self._position[0] + 1, self._position[1])
                self._heading = 'E'
            else:
                square_colors[self._position] = WHITE
                self._board.flip_color(self._position, WHITE)
                self._position = (self._position[0] - 1, self._position[1])
                self._heading = 'W'
        elif self._heading == 'E':
            if square_colors[self._position] == WHITE:
                square_colors[self._position] = BLACK
                self._board.flip_color(self._position, BLACK)
                self._position = (self._position[0], self._position[1] + 1)
                self._heading = 'S'
            else:
                square_colors[self._position] = WHITE
                self._board.flip_color(self._position, WHITE)
                self._position = (self._position[0], self._position[1] - 1)
                self._heading = 'N'
        elif self._heading == 'S':
            if square_colors[self._position] == WHITE:
                square_colors[self._position] = BLACK
                self._board.flip_color(self._position, BLACK)
                self._position = (self._position[0] - 1, self._position[1])
                self._heading = 'W'
            else:
                square_colors[self._position] = WHITE
                self._board.flip_color(self._position, WHITE)
                self._position = (self._position[0] + 1, self._position[1])
                self._heading = 'E'
        else:
            if square_colors[self._position] == WHITE:
                square_colors[self._position] = BLACK
                self._board.flip_color(self._position, BLACK)
                self._position = (self._position[0], self._position[1] - 1)
                self._heading = 'N'
            else:
                square_colors[self._position] = WHITE
                self._board.flip_color(self._position, WHITE)
                self._position = (self._position[0], self._position[1] + 1)
                self._heading = 'S'


# General Testing and Drive Code:
if __name__ == '__main__':
    langtons_ant = LangtonsAnt()
    langtons_ant.start()

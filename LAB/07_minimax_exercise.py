from itertools import groupby
from typing import Callable, Optional

import numpy as np
import FreeSimpleGUI as sg # type: ignore

from framework.gui import BoardGUI

BOARD_SIZE = 3
NEEDED_TO_WIN = 3
BLANK_IMAGE_PATH = 'tiles/gomoku_blank_scaled.png'
X_IMAGE_PATH = 'tiles/gomoku_X_scaled.png'
O_IMAGE_PATH = 'tiles/gomoku_O_scaled.png'


# Gomoku (5 in a row): O is the maximizing player (the player controlled by
# Artificial Intelligence)

# The BOARD will be represented as a numpy array
# The fields are:
# 0: empty
# 1: X
# 2: O

class GomokuBoard:
    def __init__(self, n: int = BOARD_SIZE, board: Optional[np.ndarray] = None):
        if board is None:
            self.n = n
            self.board = np.zeros((self.n, self.n), dtype=int)
        else:
            self.board = board
            self.n = board.shape[0]

    def winner(self) -> Optional[int]:
        """Return the winner of the BOARD from the point of view of the X player.

        Return winners:
        1: X wins
        2: O wins
        0: draw
        None: game is still ongoing
        """

        # check the rows
        for player, length in ((key, len(list(group))) for row in self.board
                               for key, group in groupby(row) if key != 0):
            if length >= NEEDED_TO_WIN:
                return player
        # check the columns
        for player, length in ((key, len(list(group))) for row in self.board.T
                               for key, group in groupby(row) if key != 0):
            if length >= NEEDED_TO_WIN:
                return player
        # check the diagonals (use self.board.diagonal())
        # upper left to lower right
        diagonals = (self.board.diagonal(i) for i in range(
            NEEDED_TO_WIN-self.board.shape[0], self.board.shape[0] - NEEDED_TO_WIN + 1))
        for player, length in ((key, len(list(group))) for diag in diagonals
                               for key, group in groupby(diag) if key != 0):
            if length >= NEEDED_TO_WIN:
                return player
        # lower left to upper right
        diagonals = (np.flipud(self.board).diagonal(i) for i in range(
            NEEDED_TO_WIN-self.board.shape[0], self.board.shape[0] - NEEDED_TO_WIN + 1))
        for player, length in ((key, len(list(group))) for diag in diagonals
                               for key, group in groupby(diag) if key != 0):
            if length >= NEEDED_TO_WIN:
                return player
        # check the draw
        if len(np.where(self.board == 0)[0]) == 0:
            return 0
        # otherwise, return None
        return None

    def copy(self):
        return GomokuBoard(board=self.board.copy())

    def possible_steps(self) -> np.ndarray:
        return np.argwhere(self.board == 0)

    def next_boards(self, player: int):
        """Produces a list of boards for all the possible next steps of
        player."""
        boards = []
        for row_ind, col_ind in self.possible_steps():
            next_board = self.copy()
            next_board[row_ind, col_ind] = player
            boards.append(next_board)
        return boards

    def __getitem__(self, index: tuple[int, int] | int) -> int:
        if isinstance(index, tuple):
            i, j = index
            return self.board[i][j]
        else:
            return self.board[index]

    def __setitem__(self, index: tuple[int, int] | int, item: int) -> None:
        if isinstance(index, tuple):
            i, j = index
            self.board[i][j] = item
        else:
            self.board[index] = item

    def reset(self) -> None:
        self.board = np.zeros((self.n, self.n), dtype=int)


def switch_player(player: int) -> int:
    return 3 - player


def random_move(board: GomokuBoard) -> None:
    """This strategy just makes a random allowed move on the board."""
    zero_ind = np.where(board.board == 0)
    index = np.random.randint(len(zero_ind[0]))
    row, col = zero_ind[0][index], zero_ind[1][index]
    board[row,col] = 2

# Minimax and alpha-beta use the same scoring convention:
# X wins -> -1, O wins -> +1, draw -> 0.
# Each solution is a list of boards starting with the immediate next move.

MiniMaxReturnType = tuple[Optional[int], Optional[list[GomokuBoard]]]


def minimax(board: GomokuBoard) -> None:
    """Play O's best next move using the minimax algorithm."""

    def value(board: GomokuBoard, player: int) -> MiniMaxReturnType:
        if player == 2:
            return maximize(board, player)
        return minimize(board, player)

    def minimize(board: GomokuBoard, player: int) -> MiniMaxReturnType:
        winner = board.winner()
        if winner is not None:
            if winner == 1:
                return (-1, None)
            if winner == 2:
                return (1, None)
            return (0, None)

        best_score = None
        best_solution = None

        for next_board in board.next_boards(player):
            score, solution = value(next_board, switch_player(player))
            if best_score is None or score < best_score:
                best_score = score
                best_solution = [next_board] + (solution or [])

        return (best_score, best_solution)

    def maximize(board: GomokuBoard, player: int) -> MiniMaxReturnType:
        winner = board.winner()
        if winner is not None:
            if winner == 1:
                return (-1, None)
            if winner == 2:
                return (1, None)
            return (0, None)

        best_score = None
        best_solution = None

        for next_board in board.next_boards(player):
            score, solution = value(next_board, switch_player(player))
            if best_score is None or score > best_score:
                best_score = score
                best_solution = [next_board] + (solution or [])

        return (best_score, best_solution)

    _, solution = value(board, 2)
    if solution is not None:
        board.board = solution[0].board


def alpha_beta(board: GomokuBoard) -> None:
    """Play O's best next move using minimax with alpha-beta pruning."""

    def value(board: GomokuBoard, player: int,
              alpha: float, beta: float) -> MiniMaxReturnType:
        if player == 2:
            return maximize(board, player, alpha, beta)
        return minimize(board, player, alpha, beta)

    def minimize(board: GomokuBoard, player: int,
                 alpha: float, beta: float) -> MiniMaxReturnType:
        winner = board.winner()
        if winner is not None:
            if winner == 1:
                return (-1, None)
            if winner == 2:
                return (1, None)
            return (0, None)

        best_score = None
        best_solution = None

        for next_board in board.next_boards(player):
            score, solution = value(
                next_board, switch_player(player), alpha, beta
            )
            if best_score is None or score < best_score:
                best_score = score
                best_solution = [next_board] + (solution or [])

            # MIN has a better (smaller) bound after considering this move.
            beta = min(beta, score)
            if alpha >= beta:
                break  # Remaining moves cannot improve MAX's decision.

        return (best_score, best_solution)

    def maximize(board: GomokuBoard, player: int,
                 alpha: float, beta: float) -> MiniMaxReturnType:
        winner = board.winner()
        if winner is not None:
            if winner == 1:
                return (-1, None)
            if winner == 2:
                return (1, None)
            return (0, None)

        best_score = None
        best_solution = None

        for next_board in board.next_boards(player):
            score, solution = value(
                next_board, switch_player(player), alpha, beta
            )
            if best_score is None or score > best_score:
                best_score = score
                best_solution = [next_board] + (solution or [])

            # MAX has a better (larger) bound after considering this move.
            alpha = max(alpha, score)
            if alpha >= beta:
                break  # Remaining moves cannot improve MIN's decision.

        return (best_score, best_solution)

    alpha = float('-inf')
    beta = float('inf')
    _, solution = value(board, 2, alpha, beta)
    if solution is not None:
        board.board = solution[0].board


# END OF YOUR CODE


class GameLogic:

    def __init__(self, board: GomokuBoard, move_ai: Callable):
        self.board = board
        self.move_ai = move_ai
        self.current_player = 1

    def play(self, row_ind, col_ind):
        if self.board[row_ind][col_ind] != 0:
            return None
        self.board[row_ind][col_ind] = self.current_player
        winner = self.board.winner()
        if winner is not None:
            return self.board.winner()
        self.switch_player()
        self.move_ai(self.board)
        self.switch_player()
        winner = self.board.winner()
        if winner is not None:
            return self.board.winner()

    def switch_player(self):
        self.current_player = switch_player(self.current_player)

    def reset(self):
        self.board.reset()
        self.current_player = 1


sg.change_look_and_feel('SystemDefault')

algorithms = {
    'Random move': random_move,
    'Minimax': minimax,
    'Alpha-beta search': alpha_beta
}

GOMOKU_DRAW_DICT = {
    0: ('', ('black', 'lightgrey'), BLANK_IMAGE_PATH),
    1: ('', ('black', 'lightgrey'), X_IMAGE_PATH),
    2: ('', ('black', 'lightgrey'), O_IMAGE_PATH),
}

BOARD = GomokuBoard(BOARD_SIZE)
GAME_LOGIC = GameLogic(BOARD, random_move)
BOARD_GUI = BoardGUI(BOARD, GOMOKU_DRAW_DICT) #type:ignore


def create_window(board_gui):
    layout = [[sg.Column(board_gui.board_layout)],
              [
                  sg.Frame('Algorithm settings',
                           [[
                               sg.T('Algorithm: '),
                               sg.Combo([algo for algo in algorithms],
                                        key='algorithm',
                                        readonly=True,
                                        default_value=[algo for algo in algorithms][0])
                           ]])],
              [
                  sg.Button('Restart'),
                  sg.Button('Exit')
            ]]

    window = sg.Window('Gomoku',
                       layout,
                       default_button_element_size=(10, 1),
                       auto_size_buttons=False,
                       location=(100,100),
                       font=('Helvetica', '18'))
    return window


window = create_window(BOARD_GUI)

while True:  # Event Loop
    event, values = window.Read()
    if event is None or event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if event == 'Restart':
        GAME_LOGIC.move_ai = algorithms[values['algorithm']]
        GAME_LOGIC.reset()
        BOARD_GUI.update()
    if isinstance(event, tuple):
        row, col = event
        winner = GAME_LOGIC.play(row, col)
        BOARD_GUI.update()
        if winner is not None:
            if winner == 1:
                sg.Popup('You have won, congrats!', font=('Helvetica', '18'), location=(150,150))
            elif winner == 2:
                sg.Popup('You have lost, you must be a great AI programmer! :)', font=('Helvetica', '18'), location=(150,150))
            else:
                sg.Popup("It's a draw!", font=('Helvetica', '18'), location=(150,150))
            GAME_LOGIC.reset()
            BOARD_GUI.update()


window.Close()

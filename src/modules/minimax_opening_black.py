#!/usr/bin/env python3

from utils.util import (
    generate_add, static_estimation_opening,
    invert_board
)


class MiniMaxOpeningBlack:
    """
    This class handles the logic for the opening phase of the Nine Men's Morris game for the black pieces
    using the Minimax algorithm.
    It provides methods to generate moves and evaluate the best move for the opening phase from the perspective
    of the black player.
    """
    def __init__(self):
        pass

    def minimax_opening_black(self, board, depth, is_maximizing):
        """
        Execute the Minimax algorithm for the opening phase of the game for the black player.

        Parameters:
        - board (list): The current board configuration.
        - depth (int): The maximum depth of the game tree to explore.
        - is_maximizing (bool): True if the current move is maximizing; False if minimizing.

        Returns:
        - tuple: A tuple containing the static evaluation and the best move board configuration.
        """
        board = invert_board(board)
        if depth == 0:
            return -static_estimation_opening(board), board

        possible_moves = generate_add(board)

        if is_maximizing:
            max_eval = float('-inf')
            best_move = None
            for move in possible_moves:
                eval_value, _ = self.minimax_opening_black(move, depth - 1, False)
                if eval_value > max_eval:
                    max_eval = eval_value
                    best_move = move
            return max_eval, invert_board(best_move)

        min_eval = float('inf')
        best_move = None
        for move in possible_moves:
            eval_value, _ = self.minimax_opening_black(move, depth - 1, True)
            if eval_value < min_eval:
                min_eval = eval_value
                best_move = move
        return min_eval, invert_board(best_move)

    def play_game(self, board, depth):
        """
        Initiates the play of the opening phase with the Minimax algorithm from the current board state for
        the black player.

        Parameters:
        - board (list): The current board configuration.
        - depth (int): The maximum depth of the game tree to explore.

        Returns:
        - tuple: A tuple containing the static evaluation and the best move board configuration.
        """
        return self.minimax_opening_black(board, depth, True)

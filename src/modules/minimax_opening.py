#!/usr/bin/env python3

from utils.util import generate_add, static_estimation_opening


class MiniMaxOpening:
    """
    This class handles the logic for the opening phase of the Nine Men's Morris game using the Minimax algorithm.
    It provides methods to generate moves and evaluate the best move for the opening phase.
    """
    def __init__(self):
        pass

    def minimax_opening(self, board, depth, is_maximizing):
        """
        Minimax algorithm for the opening phase.

        Parameters:
        - board (list): The current board configuration.
        - depth (int): The maximum depth of the game tree to explore.
        - is_maximizing (bool): True if the current move is maximizing; False if minimizing.

        Returns:
        - tuple: A tuple containing the static evaluation and the best move board configuration.
        """
        if depth == 0:
            return static_estimation_opening(board), board

        possible_moves = generate_add(board)

        if is_maximizing:
            max_eval = float('-inf')
            best_move = None
            for move in possible_moves:
                eval_value, _ = self.minimax_opening(move, depth - 1, False)
                if eval_value > max_eval:
                    max_eval = eval_value
                    best_move = move
            return max_eval, best_move

        min_eval = float('inf')
        best_move = None
        for move in possible_moves:
            eval_value, _ = self.minimax_opening(move, depth - 1, True)
            if eval_value < min_eval:
                min_eval = eval_value
                best_move = move
        return min_eval, best_move

    def play_game(self, board, depth):
        """
        Initiates the play of the opening phase with the Minimax algorithm from the current board state.

        Parameters:
        - board (list): The current board configuration.
        - depth (int): The maximum depth of the game tree to explore.

        Returns:
        - tuple: A tuple containing the static evaluation and the best move board configuration.
        """
        return self.minimax_opening(board, depth, True)

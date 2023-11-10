#!/usr/bin/env python3

from utils.util import (
    static_estimation_opening, generate_moves_midgame_endgame,
    static_estimation_midgame_endgame, invert_board
)


class MiniMaxGameBlack:
    """
    This class handles the logic for the midgame and endgame phases of the Nine Men's Morris game for the
    black pieces using the Minimax algorithm.
    It provides methods to generate moves and evaluate the best move for these phases from the perspective
    of the black player.
    """

    def __init__(self):
        pass

    def minimax_game_black(self, board, depth, is_maximizing):
        """
        Execute the Minimax algorithm for the midgame or endgame phase of the game for the black player.

        Parameters:
        - board (list): The current board configuration.
        - depth (int): The maximum depth of the game tree to explore.
        - is_maximizing (bool): True if the current move is maximizing; False if minimizing.

        Returns:
        - tuple: A tuple containing the static evaluation and the best move board configuration.
        """
        board = invert_board(board)
        if depth == 0:
            if board.count('W') > 3:
                return -static_estimation_midgame_endgame(board), board
            return -static_estimation_opening(board), board

        possible_moves = generate_moves_midgame_endgame(board)

        if is_maximizing:
            max_eval = float('-inf')
            best_move = None
            for move in possible_moves:
                eval_value, _ = self.minimax_game_black(move, depth - 1, False)
                if eval_value > max_eval:
                    max_eval = eval_value
                    best_move = move
            return max_eval, invert_board(best_move)

        min_eval = float('inf')
        best_move = None
        for move in possible_moves:
            eval_value, _ = self.minimax_game_black(move, depth - 1, True)
            if eval_value < min_eval:
                min_eval = eval_value
                best_move = move
        return min_eval, invert_board(best_move)

    def play_game(self, board, depth):
        """
        Initiates the play of the midgame or endgame phase with the Minimax algorithm from the current board state
        for the black player.

        Parameters:
        - board (list): The current board configuration.
        - depth (int): The maximum depth of the game tree to explore.

        Returns:
        - tuple: A tuple containing the static evaluation and the best move board configuration.
        """
        return self.minimax_game_black(board, depth, True)

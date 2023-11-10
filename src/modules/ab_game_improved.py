#!/usr/bin/env python3

from utils.util import (
    static_estimation_opening_improved, generate_move, generate_hopping,
    static_estimation_midgame_endgame_improved
)


class ABGameImproved:
    """
    This class handles the logic for the midgame and endgame phases of the Nine Men's Morris game using the
    Alpha-Beta pruning algorithm.
    It provides methods to generate moves and evaluate the best move for these phases with optimization and
    uses enhanced static estimation.
    """
    def __init__(self):
        pass

    def ab_game_improved(self, board, depth, alpha, beta, is_maximizing):
        """
        Execute the improved Alpha-Beta pruning algorithm for the midgame or endgame phase of the game.

        Parameters:
        - board (list): The current board configuration.
        - depth (int): The maximum depth of the game tree to explore.
        - alpha (float): The alpha value for pruning.
        - beta (float): The beta value for pruning.
        - is_maximizing (bool): True if the current move is maximizing; False if minimizing.

        Returns:
        - tuple: A tuple containing the static evaluation and the best move board configuration.
        """
        if depth == 0:
            if board.count('W') > 3:
                return static_estimation_midgame_endgame_improved(board), board
            return static_estimation_opening_improved(board), board

        possible_moves = generate_hopping(board) if board.count('W') == 3 else generate_move(board)

        if is_maximizing:
            max_eval = float('-inf')
            best_move = None
            for move in possible_moves:
                eval_value, _ = self.ab_game_improved(move, depth - 1, alpha, beta, False)
                if eval_value > max_eval:
                    max_eval = eval_value
                    best_move = move
                alpha = max(alpha, eval_value)
                if beta <= alpha:
                    break
            return max_eval, best_move

        min_eval = float('inf')
        best_move = None
        for move in possible_moves:
            eval_value, _ = self.ab_game_improved(move, depth - 1, alpha, beta, True)
            if eval_value < min_eval:
                min_eval = eval_value
                best_move = move
            beta = min(beta, eval_value)
            if beta <= alpha:
                break
        return min_eval, best_move

    def play_game(self, board, depth):
        """
        Initiates the play of the midgame or endgame phase with the Alpha-Beta pruning algorithm from the current
        board state.

        Parameters:
        - board (list): The current board configuration.
        - depth (int): The maximum depth of the game tree to explore.

        Returns:
        - tuple: A tuple containing the static evaluation and the best move board configuration.
        """
        return self.ab_game_improved(board, depth, float('-inf'), float('inf'), True)

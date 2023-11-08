#!/usr/bin/env python3

from utils.common_functions import (
    static_estimation_opening, generate_moves_midgame_endgame,
    static_estimation_midgame_endgame
)


class MiniMaxGame:
    def __init__(self):
        pass

    def minimax_game(self, board, depth, is_maximizing):
        """Minimax algorithm for the game phase."""
        if depth == 0:
            if board.count('W') > 3:
                return static_estimation_midgame_endgame(board), board
            return static_estimation_opening(board), board

        possible_moves = generate_moves_midgame_endgame(board)

        if is_maximizing:
            max_eval = float('-inf')
            best_move = None
            for move in possible_moves:
                eval_value, _ = self.minimax_game(move, depth - 1, False)
                if eval_value > max_eval:
                    max_eval = eval_value
                    best_move = move
            return max_eval, best_move

        min_eval = float('inf')
        best_move = None
        for move in possible_moves:
            eval_value, _ = self.minimax_game(move, depth - 1, True)
            if eval_value < min_eval:
                min_eval = eval_value
                best_move = move
        return min_eval, best_move

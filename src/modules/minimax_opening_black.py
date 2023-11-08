#!/usr/bin/env python3

from utils.common_functions import (
    generate_add, static_estimation_opening,
    invert_board
)


class MiniMaxOpeningBlack:
    def __init__(self):
        pass

    def minimax_opening_black(self, board, depth, is_maximizing):
        """Minimax algorithm for the opening phase for black."""
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

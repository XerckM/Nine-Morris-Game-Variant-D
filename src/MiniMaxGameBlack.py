#!/usr/bin/env python3

from CommonFunctions import (
    static_estimation_opening_black, generate_moves_midgame_endgame_black,
    static_estimation_midgame_endgame_black, reset_positions_evaluated,
    get_positions_evaluated
)


class MiniMaxGameBlack:
    def __init__(self):
        pass

    def minimax_game(self, board, depth, is_maximizing):
        """Minimax algorithm for the game phase."""
        if depth == 0:
            if board.count('B') > 3:
                return static_estimation_midgame_endgame_black(board), board
            return static_estimation_opening_black(board), board

        possible_moves = generate_moves_midgame_endgame_black(board)

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

    def main(self, input_file, output_file, depth):
        """Main function to read input, compute best move, and write output."""
        reset_positions_evaluated()

        with open(input_file, 'r') as f:
            board = list(f.readline().strip())

        minimax_estimate, best_move = self.minimax_game(board, depth, True)

        with open(output_file, 'w') as f:
            f.write(''.join(best_move))

        print(f"Input position: {''.join(board)}")
        print(f"Output position: {''.join(best_move)}")
        print(f"Positions evaluated by static estimation: {get_positions_evaluated()}.")
        print(f"MINIMAX estimate: {minimax_estimate}.")

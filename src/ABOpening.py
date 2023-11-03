#!/usr/bin/env python3

from CommonFunctions import (
    generate_add, static_estimation_opening,
    reset_positions_evaluated, get_positions_evaluated
)


class ABOpening:
    def __init__(self):

        pass

    def ab_opening(self, board, depth, alpha, beta, is_maximizing):
        """Alpha-Beta pruning algorithm for the opening phase."""
        if depth == 0:
            return static_estimation_opening(board), board

        possible_moves = generate_add(board)

        if is_maximizing:
            max_eval = float('-inf')
            best_move = None
            for move in possible_moves:
                eval_value, _ = self.ab_opening(move, depth - 1, alpha, beta, False)
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
            eval_value, _ = self.ab_opening(move, depth - 1, alpha, beta, True)
            if eval_value < min_eval:
                min_eval = eval_value
                best_move = move
            beta = min(beta, eval_value)
            if beta <= alpha:
                break
        return min_eval, best_move

    def main(self, input_file, output_file, depth):
        """Main function to read input, compute best move, and write output."""
        reset_positions_evaluated()

        with open(input_file, 'r') as f:
            board = list(f.readline().strip())

        ab_estimate, best_move = self.ab_opening(board, depth, float('-inf'), float('inf'), True)

        with open(output_file, 'w') as f:
            f.write(''.join(best_move))

        print(f"Input position: {''.join(board)}")
        print(f"Output position: {''.join(best_move)}")
        print(f"Positions evaluated by static estimation: {get_positions_evaluated()}.")
        print(f"ALPHA-BETA estimate: {ab_estimate}.")

#!/usr/bin/env python3

from CommonFunctions import (
    generate_add, static_estimation_opening_improved,
    reset_positions_evaluated, get_positions_evaluated
)


class MiniMaxOpeningImproved:
    def __init__(self):
        pass

    def minimax_opening(self, board, depth, is_maximizing):
        """Minimax algorithm for the opening phase with improved static estimation."""
        if depth == 0:
            return static_estimation_opening_improved(board), board

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

    def main(self, input_file, output_file, depth):
        """Main function to read input, compute best move, and write output."""
        reset_positions_evaluated()

        try:
            with open(input_file, 'r') as f:
                board = list(f.readline().strip())

            minimax_estimate, best_move = self.minimax_opening(board, depth, True)

            with open(output_file, 'w') as f:
                f.write(''.join(best_move))

            print(f"Input position: {''.join(board)}")
            print(f"Output position: {''.join(best_move)}")
            print(f"Positions evaluated by static estimation: {get_positions_evaluated()}.")
            print(f"Improved MINIMAX estimate: {minimax_estimate}.")

        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found.")
        except ValueError:
            print("Error: Depth must be an integer.")
        except Exception as e:
            print(f"Error: {e}")

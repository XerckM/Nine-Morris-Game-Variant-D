#!/usr/bin/env python3

from CommonFunctions import \
    static_estimation_opening, generate_move, \
    generate_hopping, static_estimation_midgame_endgame, \
    reset_positions_evaluated, get_positions_evaluated


class MiniMaxGame:
    def __init__(self):
        pass

    def minimax_game(self, board, depth, is_maximizing):
        """Minimax algorithm for the game phase."""
        if depth == 0:
            if board.count('W') > 3:
                return static_estimation_midgame_endgame(board), board
            else:
                return static_estimation_opening(board), board

        if board.count('W') == 3:
            possible_moves = generate_hopping(board)
        else:
            possible_moves = generate_move(board)

        if is_maximizing:
            max_eval = float('-inf')
            best_move = None
            for move in possible_moves:
                eval, _ = self.minimax_game(move, depth - 1, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in possible_moves:
                eval, _ = self.minimax_game(move, depth - 1, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
            return min_eval, best_move

    def main(self, input_file, output_file, depth):
        """Main function to read input, compute best move, and write output."""
        # Reset the counter at the start of each run
        reset_positions_evaluated()

        # Read board from input_file
        with open(input_file, 'r') as f:
            board = list(f.readline().strip())

        # Generate best move for white in game phase
        minimax_estimate, best_move = self.minimax_game(board, depth, True)

        # Write best move to output_file
        with open(output_file, 'w') as f:
            f.write(''.join(best_move))

        print(f"Input position: {''.join(board)}")
        print(f"Output position: {''.join(best_move)}")
        print(f"Positions evaluated by static estimation: {get_positions_evaluated()}.")
        print(f"MINIMAX estimate: {minimax_estimate}.")

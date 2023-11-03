#!/usr/bin/env python3

from CommonFunctions import (
    static_estimation_opening, generate_move, generate_hopping,
    static_estimation_midgame_endgame, reset_positions_evaluated,
    get_positions_evaluated
)


class ABGame:
    def __init__(self):
        pass

    def ab_game(self, board, depth, alpha, beta, is_maximizing):
        """Alpha-Beta pruning algorithm for the game phase."""
        if depth == 0:
            if board.count('W') > 3:
                return static_estimation_midgame_endgame(board), board
            return static_estimation_opening(board), board

        possible_moves = generate_hopping(board) if board.count('W') == 3 else generate_move(board)

        if is_maximizing:
            max_eval = float('-inf')
            best_move = None
            for move in possible_moves:
                eval_val, _ = self.ab_game(move, depth - 1, alpha, beta, False)
                if eval_val > max_eval:
                    max_eval = eval_val
                    best_move = move
                alpha = max(alpha, eval_val)
                if beta <= alpha:
                    break
            return max_eval, best_move

        min_eval = float('inf')
        best_move = None
        for move in possible_moves:
            eval_val, _ = self.ab_game(move, depth - 1, alpha, beta, True)
            if eval_val < min_eval:
                min_eval = eval_val
                best_move = move
            beta = min(beta, eval_val)
            if beta <= alpha:
                break
        return min_eval, best_move

    def main(self, input_file, output_file, depth):
        """Main function to read input, compute best move, and write output."""
        reset_positions_evaluated()

        with open(input_file, 'r') as f:
            board = list(f.readline().strip())

        ab_estimate, best_move = self.ab_game(board, depth, float('-inf'), float('inf'), True)

        with open(output_file, 'w') as f:
            f.write(''.join(best_move))

        print(f"Input position: {''.join(board)}")
        print(f"Output position: {''.join(best_move)}")
        print(f"Positions evaluated by static estimation: {get_positions_evaluated()}.")
        print(f"ALPHA-BETA estimate: {ab_estimate}.")

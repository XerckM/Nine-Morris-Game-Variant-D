#!/usr/bin/env python3

from CommonFunctions import close_mill, get_neighbors, generate_remove, static_estimation_opening, reset_positions_evaluated, get_positions_evaluated


class MiniMaxGame:
    def __init__(self):
        pass

    @staticmethod
    def generate_move(board):
        """Generate all possible board configurations after moving a white piece."""
        L = []
        for location in range(len(board)):
            if board[location] == 'W':
                neighbors = get_neighbors(location)
                for j in neighbors:
                    if board[j] == 'x':
                        b = board.copy()
                        b[location] = 'x'
                        b[j] = 'W'
                        if close_mill(j, b):
                            L.extend(generate_remove(b))
                        else:
                            L.append(b)
        return L

    @staticmethod
    def generate_hopping(board):
        """Generate all possible board configurations after hopping a white piece."""
        L = []
        for i in range(len(board)):
            if board[i] == 'W':
                for j in range(len(board)):
                    if board[j] == 'x':
                        b = board.copy()
                        b[i] = 'x'
                        b[j] = 'W'
                        if close_mill(j, b):
                            L.extend(generate_remove(b))
                        else:
                            L.append(b)
        return L

    def static_estimation_midgame_endgame(self, board):
        """Estimate the value of a board configuration during mid-game/endgame."""
        reset_positions_evaluated()  # Reset the counter at the start of each run
        num_white_pieces = board.count('W')
        num_black_pieces = board.count('B')
        L = self.generate_move(board)
        num_black_moves = len(L)

        if num_black_pieces <= 2:
            return 10000
        elif num_white_pieces <= 2:
            return -10000
        elif num_black_moves == 0:
            return 10000
        else:
            return 1000 * (num_white_pieces - num_black_pieces) - num_black_moves

    def minimax_game(self, board, depth, is_maximizing):
        """Minimax algorithm for the game phase."""
        if depth == 0:
            if board.count('W') > 3:
                return self.static_estimation_midgame_endgame(board), board
            else:
                return static_estimation_opening(board), board

        if board.count('W') == 3:
            possible_moves = self.generate_hopping(board)
        else:
            possible_moves = self.generate_move(board)

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

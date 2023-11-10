#!/usr/bin/env python3

from utils.common_functions import (
    get_positions_evaluated,
    reset_positions_evaluated
)
from modules.minimax_opening import MiniMaxOpening
from modules.minimax_game import MiniMaxGame
from modules.ab_opening import ABOpening
from modules.ab_game import ABGame
from modules.minimax_opening_black import MiniMaxOpeningBlack
from modules.minimax_game_black import MiniMaxGameBlack
from modules.minimax_opening_improved import MiniMaxOpeningImproved
from modules.minimax_game_improved import MiniMaxGameImproved


def open_board(input_file):
    """
    Reads the game board state from a file.

    Parameters:
    - input_file (str): The path to the file containing the initial board state.

    Returns:
    - list: The board state as a list of characters.
    """
    with open(input_file, 'r') as f:
        board = list(f.readline().strip())
    return board


def write_best_move(output_file, best_move):
    """
    Writes the best move to an output file.

    Parameters:
    - output_file (str): The path to the file where the best move will be written.
    - best_move (list): The best move determined by the game algorithm.

    Returns:
    - None
    """
    with open(output_file, 'w') as f:
        f.write(''.join(best_move))


def mini_max_opening_main(input_file, output_file, depth):
    """
    Executes the MiniMax algorithm for the opening phase and writes the best move to the output file.

    Parameters:
    - input_file (str): The path to the file containing the initial board state.
    - output_file (str): The path to the file where the best move will be written.
    - depth (int): The depth for the MiniMax algorithm.

    Returns:
    - None
    """
    game = MiniMaxOpening()
    try:
        board = open_board(input_file)

        minimax_estimate, best_move = game.minimax_opening(board, depth, True)

        write_best_move(output_file, best_move)

        print(f"Input position: {''.join(board)}")
        print(f"Output position: {''.join(best_move)}")
        print(f"Positions evaluated by static estimation: {get_positions_evaluated()}.")
        print(f"MINIMAX estimate: {minimax_estimate}.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError:
        print("Error: Depth must be an integer.")
    except Exception as e:
        print(f"Error: {e}")


def mini_max_game_main(input_file, output_file, depth):
    """
    Executes the MiniMax algorithm for the midgame/endgame phase and writes the best move to the output file.

    Parameters:
    - input_file (str): The path to the file containing the initial board state.
    - output_file (str): The path to the file where the best move will be written.
    - depth (int): The depth for the MiniMax algorithm.

    Returns:
    - None
    """
    game = MiniMaxGame()
    try:
        board = open_board(input_file)

        minimax_estimate, best_move = game.minimax_game(board, depth, True)

        write_best_move(output_file, best_move)

        print(f"Input position: {''.join(board)}")
        print(f"Output position: {''.join(best_move)}")
        print(f"Positions evaluated by static estimation: {get_positions_evaluated()}.")
        print(f"MINIMAX estimate: {minimax_estimate}.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError:
        print("Error: Depth must be an integer.")
    except Exception as e:
        print(f"Error: {e}")


def ab_opening_main(input_file, output_file, depth):
    """
    Executes the Alpha-Beta pruning algorithm for the opening phase and writes the best move to the output file.

    Parameters:
    - input_file (str): The path to the file containing the initial board state.
    - output_file (str): The path to the file where the best move will be written.
    - depth (int): The depth for the Alpha-Beta pruning algorithm.

    Returns:
    - None
    """
    game = ABOpening()
    try:
        board = open_board(input_file)

        ab_estimate, best_move = game.ab_opening(board, depth, float('-inf'), float('inf'), True)

        write_best_move(output_file, best_move)

        print(f"Input position: {''.join(board)}")
        print(f"Output position: {''.join(best_move)}")
        print(f"Positions evaluated by static estimation: {get_positions_evaluated()}.")
        print(f"ALPHA-BETA estimate: {ab_estimate}.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError:
        print("Error: Depth must be an integer.")
    except Exception as e:
        print(f"Error: {e}")


def ab_game_main(input_file, output_file, depth):
    """
    Executes the Alpha-Beta pruning algorithm for the midgame/endgame phase and writes the best move to the output file.

    Parameters:
    - input_file (str): The path to the file containing the initial board state.
    - output_file (str): The path to the file where the best move will be written.
    - depth (int): The depth for the Alpha-Beta pruning algorithm.

    Returns:
    - None
    """
    game = ABGame()
    try:
        board = open_board(input_file)

        ab_estimate, best_move = game.ab_game(board, depth, float('-inf'), float('inf'), True)

        write_best_move(output_file, best_move)

        print(f"Input position: {''.join(board)}")
        print(f"Output position: {''.join(best_move)}")
        print(f"Positions evaluated by static estimation: {get_positions_evaluated()}.")
        print(f"ALPHA-BETA estimate: {ab_estimate}.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError:
        print("Error: Depth must be an integer.")
    except Exception as e:
        print(f"Error: {e}")


def mini_max_opening_black_main(input_file, output_file, depth):
    """
    Executes the MiniMax algorithm for the opening phase from the black player's perspective and writes the best move to
    the output file.

    Parameters:
    - input_file (str): The path to the file containing the initial board state.
    - output_file (str): The path to the file where the best move will be written.
    - depth (int): The depth for the MiniMax algorithm.

    Returns:
    - None
    """
    game = MiniMaxOpeningBlack()
    try:
        board = open_board(input_file)

        minimax_estimate, best_move = game.minimax_opening_black(board, depth, True)

        write_best_move(output_file, best_move)

        print(f"Input position: {''.join(board)}")
        print(f"Output position: {''.join(best_move)}")
        print(f"Positions evaluated by static estimation: {get_positions_evaluated()}.")
        print(f"MINIMAX estimate for black: {minimax_estimate}.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError:
        print("Error: Depth must be an integer.")
    except Exception as e:
        print(f"Error: {e}")


def mini_max_game_black_main(input_file, output_file, depth):
    """
    Executes the MiniMax algorithm for the midgame/endgame phase from the black player's perspective and writes the
    best move to the output file.

    Parameters:
    - input_file (str): The path to the file containing the initial board state.
    - output_file (str): The path to the file where the best move will be written.
    - depth (int): The depth for the MiniMax algorithm.

    Returns:
    - None
    """
    game = MiniMaxGameBlack()
    try:
        board = open_board(input_file)

        minimax_estimate, best_move = game.minimax_game_black(board, depth, True)

        write_best_move(output_file, best_move)

        print(f"Input position: {''.join(board)}")
        print(f"Output position: {''.join(best_move)}")
        print(f"Positions evaluated by static estimation: {get_positions_evaluated()}.")
        print(f"MINIMAX estimate for black: {minimax_estimate}.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError:
        print("Error: Depth must be an integer.")
    except Exception as e:
        print(f"Error: {e}")


def mini_max_opening_improved_main(input_file, output_file, depth):
    """
    Executes an improved version of the MiniMax algorithm for the opening phase and writes the best move to the
    output file.

    Parameters:
    - input_file (str): The path to the file containing the initial board state.
    - output_file (str): The path to the file where the best move will be written.
    - depth (int): The depth for the improved MiniMax algorithm.

    Returns:
    - None
    """
    game = MiniMaxOpeningImproved()
    try:
        board = open_board(input_file)

        minimax_estimate, best_move = game.minimax_opening_improved(board, depth, True)

        write_best_move(output_file, best_move)

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


def mini_max_game_improved_main(input_file, output_file, depth):
    """
    Executes an improved version of the MiniMax algorithm for the midgame/endgame phase and writes the best move
    to the output file.

    Parameters:
    - input_file (str): The path to the file containing the initial board state.
    - output_file (str): The path to the file where the best move will be written.
    - depth (int): The depth for the improved MiniMax algorithm.

    Returns:
    - None
    """
    game = MiniMaxGameImproved()
    try:
        board = open_board(input_file)

        minimax_estimate, best_move = game.minimax_game_improved(board, depth, True)

        write_best_move(output_file, best_move)

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


def display_help():
    """
    Displays the help information with a list of acceptable commands.

    Returns:
    - None
    """
    commands = [
        "MiniMaxOpening",
        "MiniMaxGame",
        "ABOpening",
        "ABGame",
        "MiniMaxOpeningBlack",
        "MiniMaxGameBlack",
        "MiniMaxOpeningImproved",
        "MiniMaxGameImproved"
    ]
    print("List of acceptable commands:\n")
    for cmd in commands:
        print(f"{cmd}")
    print()


if __name__ == "__main__":
    print("Nine Morris Game Variant D\n")
    print("Instructions: Enter the command followed by the input file, output file, and depth.\n")
    print("Format: <command> <input_file_location> <output_file_location> <depth>\n")
    print("Example: \n\n "
          "MiniMaxOpening input.txt output.txt 3\n\n "
          "or \n\n "
          "MiniMaxOpeningBlack ./test/input.txt ./test/output.txt 3\n")
    print("Type '-help' for a list of acceptable commands.")
    print("Type 'exit' or 'quit' to end the program.\n")

    while True:
        reset_positions_evaluated()

        command = input(">>> ")
        parts = command.split()

        if command.lower() in ["exit", "quit"]:
            break
        elif command.lower() == "-help":
            display_help()
            continue

        if len(parts) == 4:
            input_file, output_file, depth = parts[1], parts[2], int(parts[3])

            if parts[0] == "MiniMaxOpening":
                mini_max_opening_main(input_file, output_file, depth)
            elif parts[0] == "MiniMaxGame":
                mini_max_game_main(input_file, output_file, depth)
            elif parts[0] == "ABOpening":
                ab_opening_main(input_file, output_file, depth)
            elif parts[0] == "ABGame":
                ab_game_main(input_file, output_file, depth)
            elif parts[0] == "MiniMaxOpeningBlack":
                mini_max_opening_black_main(input_file, output_file, depth)
            elif parts[0] == "MiniMaxGameBlack":
                mini_max_game_black_main(input_file, output_file, depth)
            elif parts[0] == "MiniMaxOpeningImproved":
                mini_max_opening_improved_main(input_file, output_file, depth)
            elif parts[0] == "MiniMaxGameImproved":
                mini_max_game_improved_main(input_file, output_file, depth)
            else:
                print("Invalid command. Please use the correct format.")
        else:
            print("Invalid command. Please use the correct format.")

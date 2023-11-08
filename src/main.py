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
    with open(input_file, 'r') as f:
        board = list(f.readline().strip())
    return board


def write_best_move(output_file, best_move):
    with open(output_file, 'w') as f:
        f.write(''.join(best_move))


def mini_max_opening_main(input_file, output_file, depth):
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

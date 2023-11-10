#!/usr/bin/env python3

from typing import Callable, Any
from utils.util import (
    get_positions_evaluated,
    reset_positions_evaluated,
    open_board,
    write_best_move,
    display_help,
    ascii_title
)
from modules.minimax_opening import MiniMaxOpening
from modules.minimax_game import MiniMaxGame
from modules.ab_opening import ABOpening
from modules.ab_game import ABGame
from modules.minimax_opening_black import MiniMaxOpeningBlack
from modules.minimax_game_black import MiniMaxGameBlack
from modules.minimax_opening_improved import MiniMaxOpeningImproved
from modules.minimax_game_improved import MiniMaxGameImproved


# Refactored function to handle game logic
def game_main(game_class: Callable[..., Any], input_file: str, output_file: str, depth: int):
    try:
        game = game_class()
        board = open_board(input_file)
        estimate, best_move = game.play_game(board, depth)  # Assume each game class has a `play_game` method.

        write_best_move(output_file, best_move)

        print(f"\nInput position: {''.join(board)}")
        print(f"Output position: {''.join(best_move)}")
        print(f"Positions evaluated by static estimation: {get_positions_evaluated()}.")
        print(f"{game.__class__.__name__} estimate: {estimate}.\n")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError:
        print("Error: Depth must be an integer.")
    except Exception as e:
        print(f"Error: {e}")


# Refactored dictionary to map commands to game classes
command_mapping = {
    "MiniMaxOpening": MiniMaxOpening,
    "MiniMaxGame": MiniMaxGame,
    "ABOpening": ABOpening,
    "ABGame": ABGame,
    "MiniMaxOpeningBlack": MiniMaxOpeningBlack,
    "MiniMaxGameBlack": MiniMaxGameBlack,
    "MiniMaxOpeningImproved": MiniMaxOpeningImproved,
    "MiniMaxGameImproved": MiniMaxGameImproved
}


if __name__ == "__main__":
    ascii_title()
    print("Instructions: Enter the command followed by the input file, output file, and depth.\n")
    print("Format: <command> <path_to_input_file> <path_to_output_file> <depth>\n")
    print("Type 'help' for a list of acceptable commands.")
    print("Type 'exit' or 'quit' to end the program.\n")

    while True:
        reset_positions_evaluated()

        command = input("Enter command >>> ")
        parts = command.split()

        if command.lower() in ["exit", "quit"]:
            break
        elif command.lower() == "help":
            display_help()
            continue

        if len(parts) == 4:
            input_file, output_file = parts[1], parts[2]
            try:
                depth = int(parts[3])
            except ValueError:
                print("Error: Depth must be an integer.")
                continue

            if parts[0] in command_mapping:
                game_main(command_mapping[parts[0]], input_file, output_file, depth)
            else:
                print("Invalid command. Please use the correct format.")
        else:
            print("Invalid command. Please use the correct format.")

#!/usr/bin/env python3

from MiniMaxOpening import MiniMaxOpening
from MiniMaxGame import MiniMaxGame


def mini_max_opening_main(input_file, output_file, depth):
    opening = MiniMaxOpening()
    opening.main(input_file, output_file, depth)


def mini_max_game_main(input_file, output_file, depth):
    game = MiniMaxGame()
    game.main(input_file, output_file, depth)


if __name__ == "__main__":
    while True:
        # Prompt the user for input
        command = input(">>> ")

        # Split the command into parts
        parts = command.split()

        # Check if the command is to exit the terminal
        if command.lower() in ["exit", "quit"]:
            break

        # Check if the command is valid for MiniMaxOpening
        if len(parts) == 4 and parts[0] == "MiniMaxOpening":
            input_file, output_file, depth = parts[1], parts[2], int(parts[3])
            mini_max_opening_main(input_file, output_file, depth)

        # Check if the command is valid for MiniMaxGame
        elif len(parts) == 4 and parts[0] == "MiniMaxGame":
            input_file, output_file, depth = parts[1], parts[2], int(parts[3])
            mini_max_game_main(input_file, output_file, depth)

        else:
            print("Invalid command. Please use the format:")
            print("MiniMaxOpening <input_file> <output_file> <depth>")
            print("or")
            print("MiniMaxGame <input_file> <output_file> <depth>")

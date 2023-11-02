positions_evaluated = 0  # Global variable to keep track of positions evaluated


def close_mill(pos, board):
    match pos:
        case 0:
            return (board[1] == board[0] and board[2] == board[0]) or (board[3] == board[0] and board[6] == board[0]) or (board[8] == board[0] and board[20] == board[0])
        case 1:
            return board[0] == board[1] and board[2] == board[1]
        case 2:
            return (board[0] == board[2] and board[1] == board[2]) or (board[5] == board[2] and board[7] == board[2]) or (board[13] == board[2] and board[22] == board[2])
        case 3:
            return (board[0] == board[3] and board[6] == board[3]) or (board[4] == board[3] and board[5] == board[3]) or (board[9] == board[3] and board[17] == board[3])
        case 4:
            return board[3] == board[4] and board[5] == board[4]
        case 5:
            return (board[2] == board[5] and board[7] == board[5]) or (board[3] == board[5] and board[4] == board[5]) or (board[12] == board[5] and board[19] == board[5])
        case 6:
            return (board[0] == board[6] and board[3] == board[6]) or (board[10] == board[6] and board[14] == board[6])
        case 7:
            return (board[2] == board[7] and board[5] == board[7]) or (board[11] == board[7] and board[16] == board[7])
        case 8:
            return (board[0] == board[8] and board[20] == board[8]) or (board[9] == board[8] and board[10] == board[8])
        case 9:
            return (board[8] == board[9] and board[10] == board[9]) or (board[3] == board[9] and board[17] == board[9])
        case 10:
            return (board[8] == board[10] and board[9] == board[10]) or (board[6] == board[10] and board[14] == board[10])
        case 11:
            return (board[7] == board[11] and board[16] == board[11]) or (board[12] == board[11] and board[13] == board[11])
        case 12:
            return (board[11] == board[12] and board[13] == board[12]) or (board[5] == board[12] and board[19] == board[12])
        case 13:
            return (board[11] == board[13] and board[12] == board[13]) or (board[2] == board[13] and board[22] == board[13])
        case 14:
            return (board[6] == board[14] and board[10] == board[14]) or (board[15] == board[14] and board[16] == board[14]) or (board[17] == board[14] and board[20] == board[14])
        case 15:
            return (board[14] == board[15] and board[16] == board[15]) or (board[18] == board[15] and board[21] == board[15])
        case 16:
            return (board[14] == board[16] and board[15] == board[16]) or (board[19] == board[16] and board[22] == board[16]) or (board[7] == board[16] and board[11] == board[16])
        case 17:
            return (board[3] == board[17] and board[9] == board[17]) or (board[18] == board[17] and board[19] == board[17]) or (board[14] == board[17] and board[20] == board[17])
        case 18:
            return (board[15] == board[18] and board[21] == board[18]) or (board[17] == board[18] and board[19] == board[18])
        case 19:
            return (board[17] == board[19] and board[18] == board[19]) or (board[5] == board[19] and board[12] == board[19]) or (board[16] == board[19] and board[22] == board[19])
        case 20:
            return (board[0] == board[20] and board[8] == board[20]) or (board[21] == board[20] and board[22] == board[20]) or (board[14] == board[20] and board[17] == board[20])
        case 21:
            return (board[20] == board[21] and board[22] == board[21]) or (board[15] == board[21] and board[18] == board[21])
        case 22:
            return (board[20] == board[22] and board[21] == board[22]) or (board[16] == board[22] and board[19] == board[22]) or (board[2] == board[22] and board[13] == board[22])
        case _:
            return False


def get_neighbors(position):
    match position:
        case 0: return [1, 3, 8]
        case 1: return [0, 2, 4]
        case 2: return [1, 5, 13]
        case 3: return [0, 4, 6, 9]
        case 4: return [1, 3, 5]
        case 5: return [2, 4, 7, 12]
        case 6: return [3, 7, 10]
        case 7: return [5, 6, 11]
        case 8: return [0, 9, 20]
        case 9: return [3, 8, 10, 17]
        case 10: return [6, 9, 14]
        case 11: return [7, 12, 16]
        case 12: return [5, 11, 13, 19]
        case 13: return [2, 12, 22]
        case 14: return [10, 15, 17]
        case 15: return [14, 16, 18]
        case 16: return [11, 15, 19]
        case 17: return [9, 14, 18, 20]
        case 18: return [15, 17, 21]
        case 19: return [12, 16, 22]
        case 20: return [8, 17, 21]
        case 21: return [18, 20, 22]
        case 22: return [13, 19, 21]
        case _: return []


def generate_remove(board):
    L = []
    for location in range(len(board)):
        if board[location] == 'B':
            if not close_mill(location, board):
                b = board.copy()
                b[location] = 'x'
                L.append(b)
    if not L:  # if no positions were added (all black pieces are in mills)
        for location in board:
            if board[location] == 'B':
                b = board.copy()
                b[location] = 'x'
                L.append(b)
    return L


def generate_move(board):
    L = []
    for location in range(len(board)):
        if board[location] == 'W':
            neighbors = get_neighbors(location)
            for j in neighbors:
                if board[j] == 'x':  # 'x' represents an empty spot
                    b = board.copy()
                    b[location] = 'x'
                    b[j] = 'W'
                    if close_mill(j, b):
                        L.extend(generate_remove(b))
                    else:
                        L.append(b)
    return L


def generate_hopping(board):
    # Based on the pseudocode you provided earlier
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


def static_estimation_opening(board):
    global positions_evaluated
    positions_evaluated += 1
    return board.count('W') - board.count('B')


def static_estimation_midgame_endgame(board):
    global positions_evaluated
    positions_evaluated += 1
    numWhitePieces = board.count('W')
    numBlackPieces = board.count('B')
    L = generate_move(board)  # Assuming black's move
    numBlackMoves = len(L)

    if numBlackPieces <= 2:
        return 10000
    elif numWhitePieces <= 2:
        return -10000
    elif numBlackMoves == 0:
        return 10000
    else:
        return 1000 * (numWhitePieces - numBlackPieces) - numBlackMoves


def minimax_game(board, depth, is_maximizing):
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
            eval, _ = minimax_game(move, depth-1, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in possible_moves:
            eval, _ = minimax_game(move, depth-1, True)
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move


def main(input_file, output_file, depth):
    global positions_evaluated
    positions_evaluated = 0  # Reset positions_evaluated to 0

    # Read board from input_file
    with open(input_file, 'r') as f:
        board = list(f.readline().strip())

    # Generate best move for white in midgame/endgame phase
    minimax_estimate, best_move = minimax_game(board, depth, True)

    # Write best move to output_file
    with open(output_file, 'w') as f:
        f.write(''.join(best_move))

    print(f"Input position: {''.join(board)}")
    print(f"Output position: {''.join(best_move)}")
    print(f"Positions evaluated by static estimation: {positions_evaluated}.")
    print(f"MINIMAX estimate: {minimax_estimate}.")  # Corrected this line


# If this script is run directly, it can be used as:
# python MiniMaxGame.py board3.txt board4.txt 3
if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]))

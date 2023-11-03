#!/usr/bin/env python3

# Global variable to keep track of positions evaluated
positions_evaluated = 0


def reset_positions_evaluated():
    """Reset the global counter for positions evaluated."""
    global positions_evaluated
    positions_evaluated = 0


def increment_positions_evaluated():
    """Increment the global counter for positions evaluated."""
    global positions_evaluated
    positions_evaluated += 1


def get_positions_evaluated():
    """Return the number of positions evaluated."""
    return positions_evaluated


def close_mill(position, board):
    """Check if a given position on the board is part of a mill."""
    match position:
        case 0:
            return (
                    (board[1] == board[0] and board[2] == board[0]) or
                    (board[3] == board[0] and board[6] == board[0]) or
                    (board[8] == board[0] and board[20] == board[0])
            )
        case 1: return board[0] == board[1] and board[2] == board[1]
        case 2:
            return (
                    (board[0] == board[2] and board[1] == board[2]) or
                    (board[5] == board[2] and board[7] == board[2]) or
                    (board[13] == board[2] and board[22] == board[2])
            )
        case 3:
            return (
                    (board[0] == board[3] and board[6] == board[3]) or
                    (board[4] == board[3] and board[5] == board[3]) or
                    (board[9] == board[3] and board[17] == board[3])
            )
        case 4: return board[3] == board[4] and board[5] == board[4]

        case 5:
            return (
                    (board[2] == board[5] and board[7] == board[5]) or
                    (board[3] == board[5] and board[4] == board[5]) or
                    (board[12] == board[5] and board[19] == board[5])
            )
        case 6:
            return (
                    (board[0] == board[6] and board[3] == board[6]) or
                    (board[10] == board[6] and board[14] == board[6])
            )
        case 7:
            return (
                    (board[2] == board[7] and board[5] == board[7]) or
                    (board[11] == board[7] and board[16] == board[7])
            )
        case 8:
            return (
                    (board[0] == board[8] and board[20] == board[8]) or
                    (board[9] == board[8] and board[10] == board[8])
            )
        case 9:
            return (
                    (board[8] == board[9] and board[10] == board[9]) or
                    (board[3] == board[9] and board[17] == board[9])
            )
        case 10:
            return (
                    (board[8] == board[10] and board[9] == board[10]) or
                    (board[6] == board[10] and board[14] == board[10])
            )
        case 11:
            return (
                    (board[7] == board[11] and board[16] == board[11]) or
                    (board[12] == board[11] and board[13] == board[11])
            )
        case 12:
            return (
                    (board[11] == board[12] and board[13] == board[12]) or
                    (board[5] == board[12] and board[19] == board[12])
            )
        case 13:
            return (
                    (board[11] == board[13] and board[12] == board[13]) or
                    (board[2] == board[13] and board[22] == board[13])
            )
        case 14:
            return (
                    (board[6] == board[14] and board[10] == board[14]) or
                    (board[15] == board[14] and board[16] == board[14]) or
                    (board[17] == board[14] and board[20] == board[14])
            )
        case 15:
            return (
                    (board[14] == board[15] and board[16] == board[15]) or
                    (board[18] == board[15] and board[21] == board[15])
            )
        case 16:
            return (
                    (board[14] == board[16] and board[15] == board[16]) or
                    (board[19] == board[16] and board[22] == board[16]) or
                    (board[7] == board[16] and board[11] == board[16])
            )
        case 17:
            return (
                    (board[3] == board[17] and board[9] == board[17]) or
                    (board[18] == board[17] and board[19] == board[17]) or
                    (board[14] == board[17] and board[20] == board[17])
            )
        case 18:
            return (
                    (board[15] == board[18] and board[21] == board[18]) or
                    (board[17] == board[18] and board[19] == board[18])
            )
        case 19:
            return (
                    (board[17] == board[19] and board[18] == board[19]) or
                    (board[5] == board[19] and board[12] == board[19]) or
                    (board[16] == board[19] and board[22] == board[19])
            )
        case 20:
            return (
                    (board[0] == board[20] and board[8] == board[20]) or
                    (board[21] == board[20] and board[22] == board[20]) or
                    (board[14] == board[20] and board[17] == board[20])
            )
        case 21:
            return (
                    (board[20] == board[21] and board[22] == board[21]) or
                    (board[15] == board[21] and board[18] == board[21])
            )
        case 22:
            return (
                    (board[20] == board[22] and board[21] == board[22]) or
                    (board[16] == board[22] and board[19] == board[22]) or
                    (board[2] == board[22] and board[13] == board[22])
            )
        case _: return False



def get_neighbors(position):
    """Return the neighboring positions for a given position on the board."""
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
    """Generate all possible board configurations after removing a black piece."""
    L = []
    for location in range(len(board)):
        if board[location] == 'B' and not close_mill(location, board):
            b = board.copy()
            b[location] = 'x'
            L.append(b)
    if not L:
        for location in range(len(board)):
            if board[location] == 'B':
                b = board.copy()
                b[location] = 'x'
                L.append(b)
    return L


def generate_remove_black(board):
    """Generate all possible board configurations after removing a white piece."""
    L = []
    for location in range(len(board)):
        if board[location] == 'W' and not close_mill(location, board):
            b = board.copy()
            b[location] = 'x'
            L.append(b)
    if not L:
        for location in range(len(board)):
            if board[location] == 'W':
                b = board.copy()
                b[location] = 'x'
                L.append(b)
    return L


def generate_add(board):
    """Generate all possible board configurations after adding a white piece."""
    L = []
    for location in range(len(board)):
        if board[location] == 'x':
            b = board.copy()
            b[location] = 'W'
            if close_mill(location, b):
                L.extend(generate_remove(b))
            else:
                L.append(b)
    return L


def generate_add_black(board):
    """Generate all possible board configurations after adding a black piece."""
    L = []
    for location in range(len(board)):
        if board[location] == 'x':
            b = board.copy()
            b[location] = 'B'
            if close_mill(location, b):
                L.extend(generate_remove_black(b))
            else:
                L.append(b)
    return L


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


def generate_move_black(board):
    """Generate all possible board configurations after moving a black piece."""
    L = []
    for location in range(len(board)):
        if board[location] == 'B':
            neighbors = get_neighbors(location)
            for j in neighbors:
                if board[j] == 'x':
                    b = board.copy()
                    b[location] = 'x'
                    b[j] = 'B'
                    if close_mill(j, b):
                        L.extend(generate_remove_black(b))
                    else:
                        L.append(b)
    return L


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


def generate_hopping_black(board):
    """Generate all possible board configurations after hopping a black piece."""
    L = []
    for i in range(len(board)):
        if board[i] == 'B':
            for j in range(len(board)):
                if board[j] == 'x':
                    b = board.copy()
                    b[i] = 'x'
                    b[j] = 'B'
                    if close_mill(j, b):
                        L.extend(generate_remove_black(b))
                    else:
                        L.append(b)
    return L


def static_estimation_opening(board):
    """Estimate the value of a board configuration during the opening phase."""
    # Increment the counter for positions evaluated
    increment_positions_evaluated()
    return board.count('W') - board.count('B')


def static_estimation_opening_black(board):
    """Estimate the value of a board configuration during the opening phase."""
    # Increment the counter for positions evaluated
    increment_positions_evaluated()
    return board.count('B') - board.count('W')


def static_estimation_midgame_endgame(board):
    """Estimate the value of a board configuration during mid-game/endgame for white."""
    # Increment the counter for positions evaluated
    increment_positions_evaluated()
    num_white_pieces = board.count('W')
    num_black_pieces = board.count('B')
    num_black_moves = len(generate_move(board))

    if num_black_pieces <= 2:
        return 10000
    elif num_white_pieces <= 2:
        return -10000
    elif num_black_moves == 0:
        return 10000
    else:
        return 1000 * (num_white_pieces - num_black_pieces) - num_black_moves


def static_estimation_midgame_endgame_black(board):
    """Estimate the value of a board configuration during mid-game/endgame for white."""
    # Increment the counter for positions evaluated
    increment_positions_evaluated()
    num_white_pieces = board.count('W')
    num_black_pieces = board.count('B')
    num_white_moves = len(generate_move_black(board))

    if num_white_pieces <= 2:
        return 10000
    elif num_black_pieces <= 2:
        return -10000
    elif num_white_moves == 0:
        return 10000
    else:
        return 1000 * (num_black_pieces - num_white_pieces) - num_white_moves


def generate_moves_midgame_endgame(board):
    """Generate possible moves for midgame and endgame for white pieces."""
    if board.count('W') == 3:
        possible_moves = generate_hopping(board)
    else:
        possible_moves = generate_move(board)

    return possible_moves


def generate_moves_midgame_endgame_black(board):
    """Generate possible moves for midgame and endgame for black pieces."""
    if board.count('B') == 3:
        possible_moves = generate_hopping_black(board)
    else:
        possible_moves = generate_move_black(board)

    return possible_moves


def count_mills(board, player):
    """Count the number of mills for a given player."""
    mills = 0
    for i in range(len(board)):
        if board[i] == player and close_mill(i, board):
            mills += 1
    return mills // 3  # Dividing by 3 because each mill is counted thrice


def count_potential_mills(board, player):
    """Count the number of potential mills for a given player."""
    potential_mills = 0
    for i in range(len(board)):
        if board[i] == player:
            neighbors = get_neighbors(i)
            count = sum(1 for j in neighbors if board[j] == player)
            if count == 2:
                potential_mills += 1
    return potential_mills


def count_double_mills(board, player):
    """Count the number of pieces that are part of two mills."""
    double_mills = 0
    for i in range(len(board)):
        if board[i] == player:
            mills_at_position = 0
            for j in get_neighbors(i):
                if board[j] == player and close_mill(j, board):
                    mills_at_position += 1
            if mills_at_position == 2:
                double_mills += 1
    return double_mills


def count_blocked_pieces(board, player):
    """Count the number of pieces that have no legal moves."""
    blocked_pieces = 0
    for i in range(len(board)):
        if board[i] == player:
            if player == 'W':
                moves = generate_move(board)
            else:
                moves = generate_move_black(board)
            if not moves:
                blocked_pieces += 1
    return blocked_pieces


def distance_to_conversion(board, player):
    """Calculate the distance to conversion (number of pieces more than 3)."""
    return max(0, board.count(player) - 3)


def count_center_control(board, player):
    """Count the number of pieces a player has in the central positions."""
    central_positions = [4, 10, 13, 19]
    return sum(1 for pos in central_positions if board[pos] == player)


def can_be_removed(position, board):
    """
    Determine if a piece at a given position can be removed from the board.

    A piece can be removed if it's not part of a mill or if all pieces of that player are in a mill.

    Parameters:
    - position (int): The position of the piece on the board.
    - board (list): The current board configuration.

    Returns:
    - bool: True if the piece can be removed, False otherwise.
    """
    player = board[position]
    if close_mill(position, board):
        return all(close_mill(i, board) for i, piece in enumerate(board) if piece == player)
    return True


def count_safe_pieces(board, player):
    """Count the number of pieces that are part of a mill or cannot be removed."""
    safe_pieces = 0
    for i in range(len(board)):
        if board[i] == player and (close_mill(i, board) or not can_be_removed(i, board)):
            safe_pieces += 1
    return safe_pieces


def count_threats(board, player):
    """Count the number of pieces that are threatened to be part of an opponent's mill in the next move."""
    threats = 0
    opponent = 'B' if player == 'W' else 'W'
    for i in range(len(board)):
        if board[i] == player:
            temp_board = board.copy()
            temp_board[i] = 'x'
            for j in get_neighbors(i):
                if temp_board[j] == 'x':
                    temp_board[j] = opponent
                    if close_mill(j, temp_board):
                        threats += 1
                    temp_board[j] = 'x'
    return threats


def piece_vulnerability(position, board):
    """Calculate the vulnerability of a piece at a given position."""
    player = board[position]
    opponent = 'B' if player == 'W' else 'W'
    vulnerable = 1 if board[position] != 'x' and not close_mill(position, board) else 0
    surrounded = sum(1 for neighbor in get_neighbors(position) if board[neighbor] == opponent)
    return vulnerable * surrounded


def piece_strength(position, board):
    """Calculate the strength of a piece at a given position based on potential mills."""
    player = board[position]
    strength = 0
    if board[position] == player:
        for neighbor in get_neighbors(position):
            if board[neighbor] == player:
                strength += 1
    return strength


def static_estimation_opening_improved(board):
    """
    Estimate the value of a board configuration during the opening phase.

    This improved static estimation function considers various factors such as:
    - Basic piece difference
    - Number of mills and potential mills
    - Number of double mills
    - Number of blocked pieces
    - Control of central positions
    - Number of safe pieces (pieces that are part of a mill or cannot be removed)
    - Number of pieces threatened to be part of an opponent's mill in the next move
    - Vulnerability of pieces (how exposed a piece is to potential threats)
    - Strength of pieces (how well a piece is positioned to make or block mills)

    Parameters:
    - board (list): The current board configuration.

    Returns:
    - int: The estimated value of the board configuration.
    """

    # Increment the counter for positions evaluated
    increment_positions_evaluated()

    piece_diff = board.count('W') - board.count('B')

    white_mills = count_mills(board, 'W')
    black_mills = count_mills(board, 'B')
    white_potential_mills = count_potential_mills(board, 'W')
    black_potential_mills = count_potential_mills(board, 'B')

    white_double_mills = count_double_mills(board, 'W')
    black_double_mills = count_double_mills(board, 'B')

    white_blocked = count_blocked_pieces(board, 'W')
    black_blocked = count_blocked_pieces(board, 'B')

    white_center_control = count_center_control(board, 'W')
    black_center_control = count_center_control(board, 'B')

    white_safe_pieces = count_safe_pieces(board, 'W')
    black_safe_pieces = count_safe_pieces(board, 'B')

    white_threats = count_threats(board, 'W')
    black_threats = count_threats(board, 'B')

    white_vulnerability = sum(piece_vulnerability(i, board) for i, piece in enumerate(board) if piece == 'W')
    black_vulnerability = sum(piece_vulnerability(i, board) for i, piece in enumerate(board) if piece == 'B')

    white_strength = sum(piece_strength(i, board) for i, piece in enumerate(board) if piece == 'W')
    black_strength = sum(piece_strength(i, board) for i, piece in enumerate(board) if piece == 'B')

    return (piece_diff + 2 * (white_mills - black_mills) +
            (white_potential_mills - black_potential_mills) +
            2 * (white_double_mills - black_double_mills) -
            (white_blocked - black_blocked) +
            (white_center_control - black_center_control) +
            (white_safe_pieces - black_safe_pieces) -
            (white_threats - black_threats) -
            (white_vulnerability - black_vulnerability) +
            (white_strength - black_strength))


def static_estimation_midgame_endgame_improved(board):
    """
    Estimate the value of a board configuration during mid-game/endgame for white.

    This improved static estimation function considers various factors such as:
    - Basic piece difference
    - Number of mills and potential mills
    - Number of double mills
    - Number of blocked pieces
    - Distance to conversion (number of pieces more than 3)
    - Control of central positions
    - Number of safe pieces (pieces that are part of a mill or cannot be removed)
    - Number of pieces threatened to be part of an opponent's mill in the next move
    - Vulnerability of pieces (how exposed a piece is to potential threats)
    - Strength of pieces (how well a piece is positioned to make or block mills)

    Parameters:
    - board (list): The current board configuration.

    Returns:
    - int: The estimated value of the board configuration.
    """

    # Increment the counter for positions evaluated
    increment_positions_evaluated()

    num_white_pieces = board.count('W')
    num_black_pieces = board.count('B')
    num_black_moves = len(generate_move(board))

    white_mills = count_mills(board, 'W')
    black_mills = count_mills(board, 'B')
    white_potential_mills = count_potential_mills(board, 'W')
    black_potential_mills = count_potential_mills(board, 'B')

    white_double_mills = count_double_mills(board, 'W')
    black_double_mills = count_double_mills(board, 'B')

    white_blocked = count_blocked_pieces(board, 'W')
    black_blocked = count_blocked_pieces(board, 'B')

    white_distance_conversion = distance_to_conversion(board, 'W')
    black_distance_conversion = distance_to_conversion(board, 'B')

    white_center_control = count_center_control(board, 'W')
    black_center_control = count_center_control(board, 'B')

    white_safe_pieces = count_safe_pieces(board, 'W')
    black_safe_pieces = count_safe_pieces(board, 'B')

    white_threats = count_threats(board, 'W')
    black_threats = count_threats(board, 'B')

    white_vulnerability = sum(piece_vulnerability(i, board) for i, piece in enumerate(board) if piece == 'W')
    black_vulnerability = sum(piece_vulnerability(i, board) for i, piece in enumerate(board) if piece == 'B')

    white_strength = sum(piece_strength(i, board) for i, piece in enumerate(board) if piece == 'W')
    black_strength = sum(piece_strength(i, board) for i, piece in enumerate(board) if piece == 'B')

    return (1000 * (num_white_pieces - num_black_pieces) - num_black_moves +
            2 * (white_mills - black_mills) + (white_potential_mills - black_potential_mills) +
            2 * (white_double_mills - black_double_mills) - (white_blocked - black_blocked) -
            (white_distance_conversion - black_distance_conversion) +
            (white_center_control - black_center_control) +
            (white_safe_pieces - black_safe_pieces) - (white_threats - black_threats) -
            (white_vulnerability - black_vulnerability) + (white_strength - black_strength))

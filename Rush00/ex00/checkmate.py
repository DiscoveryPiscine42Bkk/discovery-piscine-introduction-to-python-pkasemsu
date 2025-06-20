def is_in_check(board):
    # First, we need to find the position of the King (denoted by 'K').
    king_position = None
    n = len(board)  # The size of the board (assuming a square board)
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_position = (i, j)
                break
        if king_position:
            break
    
    if not king_position:
        # If we didn't find the King, return an error message.
        return "Error: King not found"

    kx, ky = king_position

    # Directions for Rook and Queen (horizontal and vertical)
    rook_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Directions for Bishop and Queen (diagonal)
    bishop_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    # Directions for Pawn (attacks diagonally)
    pawn_directions = [(-1, -1), (1, 1)]  # Attacking directions for White pawn
    
    # Check for attacks from Rooks and Queens (vertical and horizontal)
    for dx, dy in rook_directions:
        x, y = kx + dx, ky + dy
        while 0 <= x < n and 0 <= y < n:
            if board[x][y] != '.':  # If we hit a piece
                if board[x][y] == 'R' or board[x][y] == 'Q':
                    return "Success"
                break
            x, y = x + dx, y + dy

    # Check for attacks from Bishops and Queens (diagonal)
    for dx, dy in bishop_directions:
        x, y = kx + dx, ky + dy
        while 0 <= x < n and 0 <= y < n:
            if board[x][y] != '.':  # If we hit a piece
                if board[x][y] == 'B' or board[x][y] == 'Q':
                    return "Success"
                break
            x, y = x + dx, y + dy

    # Check for attacks from Pawns (diagonal attacks)
    for dx, dy in pawn_directions:
        x, y = kx + dx, ky + dy
        if 0 <= x < n and 0 <= y < n:
            if board[x][y] == 'P':
                return "Success"

    return "Fail"
board1 = [
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'K', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'P', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.']
]
print(is_in_check(board1))
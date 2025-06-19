def is_king_in_check(*rows):
    """
    Check if the King is in check on a chessboard.
    
    Args:
        *rows: Variable number of strings representing rows of the chessboard
        
    Pieces:
        'K' - King (only one allowed)
        'Q' - Queen
        'R' - Rook  
        'B' - Bishop
        'P' - Pawn
        Any other character - Empty square
    
    Returns:
        Prints "Success" if King is in check, "Fail" otherwise
    """
    try:
        if not rows:
            print("Fail")
            return
            
        board = list(rows)
        size = len(board)
        for row in board:
            if len(row) != size:
                print("Fail")
                return
        king_pos = None
        king_count = 0
        
        for i in range(size):
            for j in range(size):
                if board[i][j] == 'K':
                    king_pos = (i, j)
                    king_count += 1
        if king_count != 1:
            print("Fail")
            return
            
        king_row, king_col = king_pos
        for i in range(size):
            for j in range(size):
                piece = board[i][j]
                if piece in 'QRBP' and can_attack(board, i, j, king_row, king_col, piece):
                    print("Success")
                    return
        
        print("Fail")
        
    except Exception as e:
        print("Fail")
        return


def can_attack(board, piece_row, piece_col, king_row, king_col, piece_type):
    """Check if a piece can attack the King"""
    size = len(board)
    
    if piece_type == 'P':
        if piece_row - king_row == 1 and abs(piece_col - king_col) == 1:
            return True
            
    elif piece_type == 'R':
        if piece_row == king_row or piece_col == king_col:
            return is_path_clear(board, piece_row, piece_col, king_row, king_col)
            
    elif piece_type == 'B':
        if abs(piece_row - king_row) == abs(piece_col - king_col):
            return is_path_clear(board, piece_row, piece_col, king_row, king_col)
            
    elif piece_type == 'Q':
        if (piece_row == king_row or piece_col == king_col or 
            abs(piece_row - king_row) == abs(piece_col - king_col)):
            return is_path_clear(board, piece_row, piece_col, king_row, king_col)
    
    return False


def is_path_clear(board, start_row, start_col, end_row, end_col):
    """Check if path between two positions is clear (no pieces blocking)"""
    # Calculate direction
    row_dir = 0 if start_row == end_row else (1 if end_row > start_row else -1)
    col_dir = 0 if start_col == end_col else (1 if end_col > start_col else -1)

    curr_row, curr_col = start_row + row_dir, start_col + col_dir
    
    while curr_row != end_row or curr_col != end_col:

        if board[curr_row][curr_col] in 'KQRBP':
            return False
        curr_row += row_dir
        curr_col += col_dir
    
    return True

print("=== Testing Chess Check Function ===")

print("\nTest 1 - Queen attacks King:")
is_king_in_check(
    "Q...",
    "....",
    "....",
    "...K"
)

print("\nTest 2 - King is safe:")
is_king_in_check(
    "Q...",
    ".R..",
    "....",
    "...K"
)

print("\nTest 3 - Rook attacks King:")
is_king_in_check(
    "R..K",
    "....",
    "....",
    "...."
)

print("\nTest 4 - Bishop attacks King:")
is_king_in_check(
    "B...",
    "....",
    "....",
    "...K"
)

print("\n=== All tests completed ===")

print("\n=== How to use ===")
print("is_king_in_check('R..K', '....', '....', '....')")
print("This will print 'Success' because Rook can attack King")
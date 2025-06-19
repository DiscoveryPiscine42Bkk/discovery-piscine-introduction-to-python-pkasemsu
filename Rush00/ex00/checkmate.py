def checkmate(*board):
    if not board:
        return "Fail"
    
    size = len(board)
    if size == 0:
        return "Fail"
    
    for row in board:
        if len(row) != size:
            return "Fail"
    
    king_pos = None
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
    
    if not king_pos:
        return "Fail"
    
    king_row, king_col = king_pos
    
    for i in range(size):
        for j in range(size):
            piece = board[i][j]
            if piece in 'QRBNP':  
                if can_attack(board, i, j, king_row, king_col, piece):
                    return "Success"
    
    return "Fail"

def can_attack(board, piece_row, piece_col, king_row, king_col, piece):
    size = len(board)
    
    if piece == 'P':  
        if piece_row + 1 == king_row and abs(piece_col - king_col) == 1:
            return True
    
    elif piece == 'R':
        if piece_row == king_row or piece_col == king_col:
            return is_clear_path(board, piece_row, piece_col, king_row, king_col)
    
    elif piece == 'B':  
        if abs(piece_row - king_row) == abs(piece_col - king_col):
            return is_clear_path(board, piece_row, piece_col, king_row, king_col)
    
    elif piece == 'Q':  
       if (piece_row == king_row or piece_col == king_col or 
            abs(piece_row - king_row) == abs(piece_col - king_col)):
            return is_clear_path(board, piece_row, piece_col, king_row, king_col)
    
    elif piece == 'N':  
        dr = abs(piece_row - king_row)
        dc = abs(piece_col - king_col)
        if (dr == 2 and dc == 1) or (dr == 1 and dc == 2):
            return True
    
    return False

def is_clear_path(board, start_row, start_col, end_row, end_col):
    dr = 0 if start_row == end_row else (1 if end_row > start_row else -1)
    dc = 0 if start_col == end_col else (1 if end_col > start_col else -1)
    
    curr_row, curr_col = start_row + dr, start_col + dc
    
    while curr_row != end_row or curr_col != end_col:
        if board[curr_row][curr_col] != '.' and board[curr_row][curr_col] != ' ':
            return False
        curr_row += dr
        curr_col += dc
    
    return True

if __name__ == "__main__":
    board1 = [
        "...K....",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        ".....Q.."
    ]
    print(checkmate(*board1))  
    
    board2 = [
        "...K....",
        "........",
        ".B......",
        "........",
        "........",
        "........",
        "........",
        ".....Q.."
    ]
    print(checkmate(*board2))
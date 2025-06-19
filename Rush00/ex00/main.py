import sys
from checkmate import checkmate

def read_board(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = [line.rstrip('\n') for line in f if line.strip()]
            size = len(lines)
            if not lines or any(len(line) != size for line in lines):
                return None  
            for row in lines:
                if not all(c in 'KQRBP.' for c in row):
                    return None
            flat_board = ''.join(lines)
            if flat_board.count('K') != 1:
                return None
            return '\n'.join(lines)
    except:
        return None

def main():
    if len(sys.argv) < 2:
        return
    for file_path in sys.argv[1:]:
        board_str = read_board(file_path)
        if board_str is None:
            print("Error")
        else:
            checkmate(board_str)

if __name__ == "__main__":
    main()
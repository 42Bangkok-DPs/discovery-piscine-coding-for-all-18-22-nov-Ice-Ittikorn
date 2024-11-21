import sys
from checkmate import checkmate

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <file1.chess> [<file2.chess> ...]")
        return

    for filename in sys.argv[1:]:
        try:
            with open(filename, 'r') as file:
                board = file.read()
                checkmate(board)
        except FileNotFoundError:
            print(f"Error: File {filename} not found")

if __name__ == "__main__":
    main()
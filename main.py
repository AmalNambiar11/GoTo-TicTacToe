from game import parse_move_string, check_status

def main():
    # Example input: [(0, 0), (1, 1), (0, 1), (1, 0), (0, 2)]
    moves_string = input("Enter the series of moves (array of tuples): ")
    moves = parse_move_string(moves_string)
    check_status(moves)

main()
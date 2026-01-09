
def check_row(board, row):
    # Check if a row is filled with either X or O
    first_cell = board[row][0]

    if first_cell == 0:
        return False

    for col in range(1, 3):
        if board[row][col] != first_cell:
            return False
    
    return True


def check_col(board, col):
    # Check if a column is filled with either X or O
    first_cell = board[0][col]

    if first_cell == 0:
        return False

    for row in range(1, 3):
        if board[row][col] != first_cell:
            return False
    
    return True

def check_diag(board, row, col):
    if row == col:
        first_cell = board[0][0]

        if first_cell == 0:
            return False

        for t in range(3):
            if board[t][t] != first_cell:
                return False

        return True
    elif row + col == 2:
        first_cell = board[0][2]

        if first_cell == 0:
            return False

        for t in range(3):
            if board[t][2 - t] != first_cell:
                return False

        return True
    return False

def check_status(moves):
    # Takes a list of tuples. Returns status
    # X and O are 1 and 2 respectively
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    current_player = 1

    # Check if moves are reused

    for move in moves:
        row, col = move
        board[row][col] = current_player

        # Checks for win condition
        if check_row(board, row) or check_col(board, col) or check_diag(board, row, col):
            if current_player == 1:
                print("X wins")
                return
            elif current_player == 2:
                print("O wins")
                return

        current_player = 3 - current_player # Swaps 1 and 2
    
    # TODO: Check for excess moves

    if len(moves) == 9:
        print("Draw")
    else:
        print("In Progress")


def parse_move_string(moves_string):
    if not ( moves_string[0] == "[" and moves_string[-1] == "]" ):
        print("No square brackets")
        return # No square brackets
    
    moves_string = moves_string[1:-1]

    # First part is an empty string
    move_tuple_list = moves_string.split("(")[1:]
    # TODO: Could there be a trailing comma?

    moves = []

    for move_tuple in move_tuple_list:
        move_fragments = move_tuple.split(",")

        if len(move_fragments) < 2:
            return # Not enough
        
        # TODO: Check if they are valid ints
        row = int(move_fragments[0].strip())
        col = int(move_fragments[1].strip()[0])

        moves.append((row, col))
    
    return moves

def main():
    # Example input: [(0, 0), (1, 1), (0, 1), (1, 0), (0, 2)]
    moves_string = input("Enter the series of moves (array of tuples): ")
    moves = parse_move_string(moves_string)
    check_status(moves)

main()
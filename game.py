
def check_triplet(triple):
    first_cell = triple[0]

    if first_cell == 0:
        return False

    for i in range(1, 3):
        if triple[i] != first_cell:
            return False
    
    return True

def check_row(board, row):
    # Check if a row is filled with either X or O 
    row = board[row] 
    return check_triplet(row)


def check_col(board, col):
    # Check if a column is filled with either X or O
    column = [ board[row][col] for row in range(3) ]
    return check_triplet(column)

def check_diag(board, row, col):
    if row == col:
        diag = [ board[i][i] for i in range(3) ]
    elif row + col == 2:
        diag = [ board[i][2 - i] for i in range(3) ]
    else:
        return False
    
    return check_triplet(diag)

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


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
        if check_row(board, row) or check_col(board, col):
            if current_player == 1:
                print("X wins")
            elif current_player == 2:
                print("O wins")

        current_player = 3 - current_player # Swaps 1 and 2
    
    if len(moves) == 9:
        print("Draw")
    else:
        print("In Progress")


def main():

    pass
from game import check_triplet, parse_move_string, check_status

def test_check_triplet():
    test_set = [
        # Arrays
        [0, 0, 1],      # False
        [2, 2, 2],      # True
        [1, 2, 2, 2],   # False
        [2, 2, 2, 2],   # False
        # Tuples
        (0, 1, 1),      # False
        (1, 1, 1),      # True  
    ]

    expectation_set = [
        False,
        True,
        False,
        False,
        False,
        True,
    ]

    all_success = True

    for test, expected in zip(test_set, expectation_set):
        result = check_triplet(test)

        if not result == expected:
            all_success = False

            print(test, "Result: ", result, "Expected: ", expected)
    
    if all_success:
        print("SUCCESS!")

def test_game():
    test_set = [
        "[(0, 0), (1, 1), (0, 1), (1, 0), (0, 2)]", # X Wins
        "[(1, 1), (0, 0), (2, 0), (0, 2), (0, 1), (2, 1), (1, 2), (1, 0), (2, 2)]", # Draw
        "[(1, 1), (0, 0), (2, 0), (0, 2), (0, 1)]", # In Progress
        "[(1, 1), (0, 0), (0, 2), (2, 0), (0, 1), (2, 1), (1, 2), (1, 0), (2, 2)]", # O Wins
        "[(1, 2), (1, 1), (0, 2), (2, 2), (0, 1), (0, 0)]", # O Wins (diagonal)
    ]

    for moves_string in test_set:
        moves = parse_move_string(moves_string)
        check_status(moves)

def test_all():
    test_check_triplet()
    test_game()

test_all()
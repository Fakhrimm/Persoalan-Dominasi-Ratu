from board import *


def bruteforce():
    """Return number of iterations and list of Queen's positions needed to cover an 8 x 8 board"""

    n = 8

    # Initialize board
    board = [[0 for i in range(n)] for j in range(n)]

    # Initialize Queen's positions
    queens = []

    # Initialize number of iterations
    num_iterations = 0

    # Loop until all squares are covered
    for q1 in range(n*n - 4):
        for q2 in range(q1 + 1, n*n - 3):
            for q3 in range(q2 + 1, n*n - 2):
                for q4 in range(q3 + 1, n*n - 1):
                    for q5 in range(q4 + 1, n*n):
                        # Increment number of iterations
                        num_iterations += 1

                        # Place Queen's
                        board = place_queen(board, q1 // n, q1 % n, 1)
                        board = place_queen(board, q2 // n, q2 % n, 2)
                        board = place_queen(board, q3 // n, q3 % n, 3)
                        board = place_queen(board, q4 // n, q4 % n, 4)
                        board = place_queen(board, q5 // n, q5 % n, 5)

                        # Check if all squares are covered
                        if is_covered(board):
                            queens = [q1, q2, q3, q4, q5]
                            print('Found solution:')
                            print_board(queens)
                            print(queens)
                            print(num_iterations)
                            return

                        # Reset board
                        board = [[0 for i in range(n)] for j in range(n)]

    print('No solution found')
    print(num_iterations)


def bruteforce_k_equal_3():
    n = 8

    # Initialize board
    board = [[0 for i in range(n)] for j in range(n)]

    # Initialize Queen's positions
    queens = []

    # Initialize number of iterations
    num_iterations = 0

    # Loop until all squares are covered
    for q1 in range(n*n - 2):
        for q2 in range(q1 + 1, n*n - 1):
            for q3 in range(q2 + 1, n*n):
                # Increment number of iterations
                num_iterations += 1

                # Place Queen's
                board = place_queen(board, q1 // n, q1 % n, 1)
                board = place_queen(board, q2 // n, q2 % n, 2)
                board = place_queen(board, q3 // n, q3 % n, 3)

                # Check if all squares are covered
                if is_covered(board):
                    num_queens_needed = 5
                    queens = [q1, q2, q3]
                    print_board_raw(board)
                    print(queens)
                    print(num_iterations)

                # Reset board
                board = [[0 for i in range(n)] for j in range(n)]

    print('No solution found')
    print(num_iterations)


def bruteforce_k_equal_4():
    n = 8

    # Initialize board
    board = [[0 for i in range(n)] for j in range(n)]

    # Initialize Queen's positions
    queens = []

    # Initialize number of iterations
    num_iterations = 0

    # Loop until all squares are covered
    for q1 in range(n*n - 3):
        for q2 in range(q1 + 1, n*n - 2):
            for q3 in range(q2 + 1, n*n - 1):
                for q4 in range(q3 + 1, n*n):
                    # Increment number of iterations
                    num_iterations += 1

                    # Place Queen's
                    board = place_queen(board, q1 // n, q1 % n, 1)
                    board = place_queen(board, q2 // n, q2 % n, 2)
                    board = place_queen(board, q3 // n, q3 % n, 3)
                    board = place_queen(board, q4 // n, q4 % n, 4)

                    # Check if all squares are covered
                    if is_covered(board):
                        num_queens_needed = 5
                        queens = [q1, q2, q3, q4]
                        print_board_raw(board)
                        print(queens)
                        print(num_iterations)

                    # Reset board
                    board = [[0 for i in range(n)] for j in range(n)]

    print('No solution found')
    print(num_iterations)


def bruteforce_num_of_solution():
    num_solution = 0
    n = 8

    # Initialize board
    board = [[0 for i in range(n)] for j in range(n)]

    # Initialize Queen's positions
    queens = []

    # Initialize number of iterations
    num_iterations = 0

    # Loop until all squares are covered
    for q1 in range(n*n - 4):
        for q2 in range(q1 + 1, n*n - 3):
            for q3 in range(q2 + 1, n*n - 2):
                for q4 in range(q3 + 1, n*n - 1):
                    for q5 in range(q4 + 1, n*n):
                        # Increment number of iterations
                        num_iterations += 1

                        # Place Queen's
                        board = place_queen(board, q1 // n, q1 % n, 1)
                        board = place_queen(board, q2 // n, q2 % n, 2)
                        board = place_queen(board, q3 // n, q3 % n, 3)
                        board = place_queen(board, q4 // n, q4 % n, 4)
                        board = place_queen(board, q5 // n, q5 % n, 5)

                        # Check if all squares are covered
                        if is_covered(board):
                            num_solution += 1

                        # Reset board
                        board = [[0 for i in range(n)] for j in range(n)]

    print('Number of solution found: ' + str(num_solution))

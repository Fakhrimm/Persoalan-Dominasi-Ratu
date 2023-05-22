import copy


def place_queen(board, row, col, queen_num):
    n = len(board)

    q = queen_num

    board[row][col] = q

    for k in range(n):
        board[row][k] = q
        board[k][col] = q
        if row + k < n and col + k < n:
            board[row + k][col + k] = q
        if row - k >= 0 and col - k >= 0:
            board[row - k][col - k] = q
        if row + k < n and col - k >= 0:
            board[row + k][col - k] = q
        if row - k >= 0 and col + k < n:
            board[row - k][col + k] = q

    return board


def is_covered(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                return False
    return True


def print_board_raw(board):
    n = len(board)
    for i in range(n):
        print(board[i])


def print_board(queen_pos):
    board = [[0 for i in range(8)] for j in range(8)]
    n = len(board)
    for i in range(n):
        for j in range(n):
            if i*n + j in queen_pos:
                print('Q', end=' ')
            else:
                print(board[i][j], end=' ')
        print()


def count_zero(board):
    n = len(board)
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                count += 1
    return count


def place_queen_grouped(board, queen_pos):
    for i in range(len(queen_pos)):
        board = place_queen(board, queen_pos[i] // 8, queen_pos[i] % 8, 1)
    return board


def get_score(board, queen_pos):

    board_copy = copy.deepcopy(board)

    return count_zero(place_queen_grouped(board_copy, queen_pos))

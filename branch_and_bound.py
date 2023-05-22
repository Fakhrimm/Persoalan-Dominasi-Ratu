from queue import PriorityQueue
from board import *


def branch_and_bound():
    iterations = 0

    board = [[0 for i in range(8)] for j in range(8)]

    prio_queue = PriorityQueue()

    for i in range(64):
        iterations += 1
        score = get_score(board, [i])
        prio_queue.put((score, [i]))

    while not prio_queue.empty():
        score, queen_pos = prio_queue.get()
        for i in range(64):
            if i not in queen_pos:
                iterations += 1
                new_queen_pos = copy.deepcopy(queen_pos)
                new_queen_pos.append(i)
                score = get_score(board, new_queen_pos)
                if score == 0:
                    print_board(new_queen_pos)
                    print(new_queen_pos)
                    print("Iterations: ", iterations)
                    return
                prio_queue.put((score, new_queen_pos))

    print("No solution found")


def branch_and_bound_all_solution():
    solution_num = 0

    iterations = 0

    board = [[0 for i in range(8)] for j in range(8)]

    prio_queue = PriorityQueue()

    for i in range(64):
        iterations += 1
        score = get_score(board, [i])
        prio_queue.put((score, [i]))

    while not prio_queue.empty():
        score, queen_pos = prio_queue.get()
        for i in range(queen_pos[len(queen_pos) - 1] + 1, 64):
            iterations += 1
            new_queen_pos = copy.deepcopy(queen_pos)
            new_queen_pos.append(i)
            score = get_score(board, new_queen_pos)
            if score == 0:
                solution_num += 1
                continue
            if len(new_queen_pos) < 5:
                prio_queue.put((score, new_queen_pos))

    print("Number of solutions: ", solution_num)

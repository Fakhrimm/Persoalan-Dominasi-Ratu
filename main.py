from bruteforce import *
from branch_and_bound import *
import time


def main():
    """Main function"""

    # Run bruteforce algorithm
    # queens, num_iterations = bruteforce()

    # Print results
    # print("Queens: ", queens)
    # print("Number of iterations: ", num_iterations)
    # print_board(queens)
    start = time.time()
    branch_and_bound()
    end = time.time()
    print("Time taken: ", end - start)
    # print(branch_and_bound())

    # res = branch_and_bound()
    # print_board(res[0])


if __name__ == "__main__":
    main()

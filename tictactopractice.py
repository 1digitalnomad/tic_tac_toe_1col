
# print the boards only function
def print_2D(b):
    for i in range(len(b)):  # will look 3 times
        # will print first ten go to the next for loop. Don't return to next line.
        print("[", end=" ")
        for i in b[i]:  # will loop 3 times before going up the the first loop.
            # will print every element in the current array, i.e. o,o,x
            print(i, end=" ")
        print("]")  # will print after each row


def main():
    boards = [
        [["0", "X", "0"]] * 3,
        [['0', '0', 'X'], ['0', 'X', '0'], ['X', '0', '0']],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[i for i in range(1, 4)]] * 3,
        [
            [i for i in range(1, 4)],
            [i for i in range(4, 7)],
            [i for i in range(7, 10)]
        ]
    ]

    for b in boards:
        print_2D(b)
        print("=" * 10)


main()

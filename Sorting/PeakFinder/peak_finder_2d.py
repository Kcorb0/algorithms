# Two-dimensional peak finder algorithm

"""
Example:

    0 c 0 0 0
    d a b 0 0
    0 e 0 0 0
    0 0 0 0 0

    a is only a peak if:
        a >= b and a >= c and a >= d and a >= e

"""

# Finding the peak using the greedy ascent algorithm
# Picks direction based on starting point follows the largest number till there are no larger number around the current number
def greedy_ascent(arr):

    row = len(arr) // 2
    col = len(arr[0]) // 2
    next_item = arr[row][col]

    while True:
        # Left
        if next_item < arr[row][col - 1]:
            print("left")
            col -= 1
        # right
        elif next_item < arr[row][col + 1]:
            print("right")
            col += 1
        # up
        elif next_item < arr[row - 1][col]:
            print("up")
            row -= 1
        # down
        elif next_item < arr[row + 1][col]:
            print("down")
            row += 1
        else:
            return next_item

        next_item = arr[row][col]


test_arr1 = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 2, 3, 1, 1, 1],
    [1, 1, 6, 4, 1, 1],
    [1, 9, 7, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

print(f"\nA peak is {greedy_ascent(test_arr1)}")


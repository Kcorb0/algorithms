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
# Time complexity O(n^2)
def greedy_ascent():
    return None

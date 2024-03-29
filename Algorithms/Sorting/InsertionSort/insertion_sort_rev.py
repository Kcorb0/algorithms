import random as rd
from sorting_vis import vis_print
import time


def insertion_sort_reversed(arr):
    for i in range(1, len(arr)):
        # Initialize the starting key and set variable
        # for prior key index
        key = arr[i]
        j = i - 1
        # Move any elements that are less than the key
        # one index position ahead of their current posNo
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


inpsize = 100
input_arr = list(range(inpsize))
rd.shuffle(input_arr)

print(insertion_sort_reversed(input_arr))

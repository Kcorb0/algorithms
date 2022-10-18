import random as rd
from sorting_vis import vis_print
import time


def insertion_sort(arr):

    h = max(arr)

    for i in range(1, len(arr)):
        # Initialize the starting key and set variable
        # for prior key index
        key = arr[i]
        j = i - 1
        # Move any elements that are greater than the key
        # one index position ahead of their current pos
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        for k in vis_print(arr, h):
            print(k)
        # time.sleep(0.01)

        arr[j + 1] = key

    return arr


inpsize = 1000
input_arr = list(range(inpsize))
rd.shuffle(input_arr)

# print(f"Input: {input_arr}")
# print(f"Output: {insertion_sort(input_arr)}")

insertion_sort(input_arr)

import time
import random as rd

array_example1d = [2, 2, 6, 2, 2, 0, 5, 4, 9, 2]

# One-dimensional version
# Time Complexity: 0(n)
def peak_finder_1d(arr):

    for idx, i in enumerate(arr):
        if idx != 0 and idx != len(arr) - 1:
            if i >= arr[idx - 1] and i >= arr[idx + 1]:
                return i


peak_finder_1d(array_example1d)


# Using divide and conqour
# Time Complexity 0 (log2 n)
def peak_finder_1d_dc(arr):

    n = len(arr)

    # Check left num
    while len(arr) > 1:

        if arr[n // 2] < arr[n // 2 - 1]:
            arr = arr[: n // 2]
            n = len(arr)
        # Check right num
        elif arr[n // 2] < arr[n // 2 + 1]:
            arr = arr[n // 2 :]
            n = len(arr)
        # If neither left or right is larger, a peak has been found
        else:
            return arr[n // 2]


peak_finder_1d_dc(array_example1d)


# Testing time to run
test_array = list(range(100000000)) + [1]
# rd.shuffle(test_array)
run_times = 100

print("Time Test for {} inputs".format(len(test_array)))
print("\nBasic peak finder")
time1 = time.time()
peak_finder_1d(test_array)
print(time.time() - time1)

print("\nUsing Divide and Conqour")
time2 = time.time()
peak_finder_1d_dc(test_array)
print(time.time() - time2)

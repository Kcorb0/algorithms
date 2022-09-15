import random as rand


def selection_sort(arr):
    for i in range(len(arr)):
        # s will store the next smallest value starting with j as we don't know the smallest yet
        s = arr[i]
        # sp will store the position of the next smallest
        sp = i

        # Check elements after ith element of the array this will reduce the searching time by 1 for each iteration
        for x in range(i, len(arr)):
            if arr[x] < s:
                s = arr[x]
                sp = x

        # After finding the next smallest number we can swap the values
        arr[sp] = arr[i]
        arr[i] = s

    return arr


# growth is: n - n^2 - n
# Time complexity: O(n^2)
# Space Complexity: O(1)

input_arr = list(range(100))
rand.shuffle(input_arr)
print(selection_sort(input_arr))

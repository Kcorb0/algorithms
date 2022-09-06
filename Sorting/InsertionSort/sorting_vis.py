import sys, os
import random


def vis_print(arr, height):
    os.system("cls")
    vis_arr = []
    level = 0

    while level <= height:
        row = []

        for i in arr:

            if i >= level:
                row.append("| ")
            else:
                row.append("  ")

        vis_arr.append(f'{"".join(row)}')
        level += 1

    return vis_arr


if __name__ == "__main__":
    os.system("cls")
    testr = list(range(100))
    random.shuffle(testr)
    h = max(testr)
    for i in vis_print(testr, h):
        print(i)

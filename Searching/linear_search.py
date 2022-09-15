def linear_search(arr, value):
    for i in range(len(arr) - 1):
        if arr[i] == value:
            return f"Position {i}: {arr[i]}"

    return None


arr = [5, 1, 2, 2, 6, 6]
print(linear_search(arr, 6))

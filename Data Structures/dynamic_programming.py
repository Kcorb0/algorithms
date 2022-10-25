# Fib example with recursion


def nthfib(n):

    # Base case
    if n == 0:
        return 0
    if n == 1:
        return 1

    return nthfib(n - 1) + nthfib(n - 2)


print(nthfib(1))
print(nthfib(2))
print(nthfib(3))
print(nthfib(4))
print(nthfib(5))
print(nthfib(6))

def climbStairs(n):

    # MEMOIZATION
    # subproblems, key = arg to function, value = return value

    def climb(n, subproblems={}):

        # RETURN EXISTING SUB PROBLEMS
        if n in subproblems:
            return subproblems[n]

        # BASE CASE
        if n <= 1:
            return 1

        # STORE PROBLEM
        subproblems[n] = climb(n - 1) + climb(n - 2)

        # RECURSIVE CASE
        return subproblems[n]

    return climb(n)

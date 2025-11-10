def bell_number(n):
    """Return the nth Bell number (number of ways to partition a set of n elements)."""
    if n < 0:
        return 0
    if n == 0:
        return 1
    # Use Bell triangle method
    bell = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    bell[0][0] = 1
    for i in range(1, n + 1):
        bell[i][0] = bell[i - 1][i - 1]
        for j in range(1, i + 1):
            bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]
    return bell[n][0]

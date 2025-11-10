def bell_number(n):
    # if not isinstance(n, int):
    #     if isinstance(n, float) and n.is_integer():
    #         n = int(n)
    #     else:
    #         return -1
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 2:
        return 2
    bell = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    bell[0][0] = 1
    for i in range(1, n + 1):
        bell[i][0] = bell[i - 1][i - 1]
        for j in range(1, i + 1):
            bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]
    return bell[n][0]
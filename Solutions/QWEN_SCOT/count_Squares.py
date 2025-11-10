def count_Squares(m, n):
    if m <= 0 or n <= 0:
        return 0
    total = 0
    min_side = min(m, n)
    for i in range(1, min_side + 1):
        total += (m - i + 1) * (n - i + 1)
    return total
def count_Squares(m, n):
    """Count the number of squares in a m x n rectangle."""
    if m <= 0 or n <= 0:
        return 0
    total = 0
    min_side = min(m, n)
    for i in range(1, min_side + 1):
        total += (m - i + 1) * (n - i + 1)
    return total

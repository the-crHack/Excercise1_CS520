def count_Squares(m, n):
    """Count the number of squares in an m x n rectangle."""
    count = 0
    for i in range(1, min(m, n) + 1):
        count += (m - i + 1) * (n - i + 1)
    return count

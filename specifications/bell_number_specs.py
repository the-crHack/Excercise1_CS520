# 1. Negative input handling
assert (n < 0) == (res == 0)

# 2. Base case B(0) = 1
assert (n == 0) == (res == 1)

# 3. Base case B(1) = 1
assert (n == 1) == (res == 1)

# 4. Known values for small n
assert (n == 2 and res == 2) or (n == 3 and res == 5) or (n == 4 and res == 15) or (n not in [2, 3, 4])

# 5. Result is always positive for n >= 0
assert (n >= 0) == (res > 0)

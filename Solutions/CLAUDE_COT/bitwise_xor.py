def bitwise_xor(tup1, tup2):
    """Perform bitwise XOR operation across corresponding elements of tuples."""
    return tuple(map(lambda x, y: x ^ y, tup1, tup2))

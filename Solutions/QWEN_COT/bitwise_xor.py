def bitwise_xor(tup1, tup2):
    """Perform bitwise XOR operation across the given tuples element-wise."""
    return tuple(a ^ b for a, b in zip(tup1, tup2))

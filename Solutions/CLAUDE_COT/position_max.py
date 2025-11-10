def position_max(lst):
    """Find all indices where the maximum value occurs."""
    if not lst:
        return []
    max_val = max(lst)
    return [i for i, val in enumerate(lst) if val == max_val]

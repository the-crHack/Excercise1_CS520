def position_max(lst):
    """Find all index positions of the maximum values in a given list."""
    if not lst:
        return []
    max_val = max(lst)
    return [i for i, val in enumerate(lst) if val == max_val]

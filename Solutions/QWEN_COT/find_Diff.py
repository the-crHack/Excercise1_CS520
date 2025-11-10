def find_Diff(arr):
    """Find the difference between highest and least frequencies in a given array."""
    if not arr:
        return 0
    from collections import Counter
    freq = Counter(arr)
    frequencies = list(freq.values())
    return max(frequencies) - min(frequencies)

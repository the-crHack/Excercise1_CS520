def find_Diff(arr):
    """Find the difference between highest and lowest frequency in array."""
    if not arr:
        return 0
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    frequencies = list(freq.values())
    return max(frequencies) - min(frequencies)

def find_Diff(arr):
    if not arr:
        return 0
    freq = Counter(arr)
    frequencies = list(freq.values())
    return max(frequencies) - min(frequencies)
def find_peak(arr):
    """Find a peak element in the given array (an element greater than its neighbors)."""
    if not arr:
        return None
    n = len(arr)
    if n == 1:
        return arr[0]
    if arr[0] > arr[1]:
        return arr[0]
    if arr[n - 1] > arr[n - 2]:
        return arr[n - 1]
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return arr[i]
    # In case no peak found (shouldn't happen in typical cases with distinct neighbors),
    # return the maximum as fallback
    return max(arr)

def find_peak(arr):
    """Find a peak element in the array (element greater than its neighbors)."""
    n = len(arr)
    
    if n == 0:
        return None
    if n == 1:
        return arr[0]
    
    # Check first element
    if arr[0] >= arr[1]:
        return arr[0]
    
    # Check last element
    if arr[n-1] >= arr[n-2]:
        return arr[n-1]
    
    # Check middle elements
    for i in range(1, n-1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            return arr[i]
    
    return None

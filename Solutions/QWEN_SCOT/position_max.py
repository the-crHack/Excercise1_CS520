# position_max.py

def position_max(lst):

    if not lst:
        return []

    first_val = lst[0]
    all_same = True
    for val in lst:
        if val != first_val:
            all_same = False
            break
    if all_same:
        return list(range(len(lst)))

    if len(lst) == 1:
        return [0]

    max_val = lst[0]
    n = len(lst)

    for i in range(1, n):
        if lst[i] > max_val:
            max_val = lst[i]

    max_positions = []
    for i in range(n):
        if lst[i] == max_val:
            max_positions.append(i)

    return max_positions

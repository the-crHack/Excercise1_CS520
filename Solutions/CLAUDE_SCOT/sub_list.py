def sub_list(lst1, lst2):
    """Subtract corresponding elements of two lists using map and lambda."""
    return list(map(lambda x, y: x - y, lst1, lst2))

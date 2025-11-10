def sub_list(list1, list2):
    """Subtract two lists element-wise using map and lambda function."""
    return list(map(lambda x, y: x - y, list1, list2))

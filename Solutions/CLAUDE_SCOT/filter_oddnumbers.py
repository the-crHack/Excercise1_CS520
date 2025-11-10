def filter_oddnumbers(lst):
    """Filter odd numbers from a list using lambda function."""
    return list(filter(lambda x: x % 2 != 0, lst))

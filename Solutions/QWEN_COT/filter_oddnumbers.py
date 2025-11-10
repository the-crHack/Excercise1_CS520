def filter_oddnumbers(nums):
    """Filter odd numbers using lambda function."""
    return list(filter(lambda x: x % 2 != 0, nums))

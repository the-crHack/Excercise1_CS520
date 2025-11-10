def month_season(month, day):
    """Return the season for the given month and day (Northern Hemisphere)."""
    if month in [1, 2] or (month == 3 and day < 20) or (month == 12 and day >= 21):
        return "Winter"
    elif month in [4, 5] or (month == 3 and day >= 20) or (month == 6 and day < 21):
        return "Spring"
    elif month in [7, 8] or (month == 6 and day >= 21) or (month == 9 and day < 22):
        return "Summer"
    elif month in [10, 11] or (month == 9 and day >= 22) or (month == 12 and day < 21):
        return "Autumn"
    else:
        return "Invalid date"

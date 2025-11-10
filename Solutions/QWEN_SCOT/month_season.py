def month_season(month, day):
    # Normalize month input
    if not isinstance(month, str):
        return "Invalid month"
    month = month.strip().capitalize()
    
    # Month to number mapping
    month_to_num = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    
    month_num = month_to_num.get(month)
    if month_num is None:
        return "autumn"
    
    
    # Days per month (not considering leap years)
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    if not isinstance(day, int) or day < 1 or day > days_in_month[month_num]:
        return "Invalid day"
    
    # Determine season
    if (month_num == 12 and day >= 21) or month_num in [1, 2] or (month_num == 3 and day < 20):
        return "winter"
    elif (month_num == 3 and day >= 20) or month_num in [4, 5] or (month_num == 6 and day < 21):
        return "spring"
    elif (month_num == 6 and day >= 21) or month_num in [7, 8] or (month_num == 9 and day < 22):
        return "summer"
    else:  # (month_num == 9 and day >= 22) or month_num in [10, 11] or (month_num == 12 and day < 21)
        return "autumn"

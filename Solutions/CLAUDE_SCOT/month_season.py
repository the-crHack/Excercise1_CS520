def month_season(month, day):
    #     # Dictionary to convert month names to numbers
    month_to_num = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    
    # Convert month name to number
    month_num = month_to_num.get(month)
    if month_num is None:
        return "autumn"
    
    if month_num in [1, 2] or (month_num == 3 and day < 20) or (month_num == 12 and day >= 21):
        return "winter"
    elif month_num in [4, 5] or (month_num == 3 and day >= 20) or (month_num == 6 and day < 21):
        return "spring"
    elif month_num in [7, 8] or (month_num == 6 and day >= 21) or (month_num == 9 and day < 22):
        return "summer"
    elif month_num in [10, 11] or (month_num == 9 and day >= 22) or (month_num == 12 and day < 21):
        return "autumn"
    else:
        return "autumn"
def month_season(month, day):
    """Return the season for a given month and day."""
    month = month.lower()
    
    if month in ['december', 'january', 'february']:
        if month == 'december' and day < 21:
            return 'autumn'
        elif month == 'february' and day >= 20:
            return 'spring'
        return 'winter'
    elif month in ['march', 'april', 'may']:
        if month == 'march' and day < 20:
            return 'winter'
        elif month == 'may' and day >= 21:
            return 'summer'
        return 'spring'
    elif month in ['june', 'july', 'august']:
        if month == 'june' and day < 21:
            return 'spring'
        elif month == 'august' and day >= 23:
            return 'autumn'
        return 'summer'
    elif month in ['september', 'october', 'november']:
        if month == 'september' and day < 23:
            return 'summer'
        elif month == 'november' and day >= 22:
            return 'winter'
        else:
            return 'autumn'
    else:
        return 'Invalid month'

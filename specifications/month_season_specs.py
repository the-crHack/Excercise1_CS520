# Specification 1: Invalid month handling
assert not (month.lower() not in ["january", "february", "march", "april", "may", 
                                   "june", "july", "august", "september", "october", 
                                   "november", "december"])

# Specification 2: Invalid day handling
assert (isinstance(day, int) and 1 <= day <= days_in_month[month_num]) == (res != "Invalid day")
# or explicitly
assert (not isinstance(day, int) or day < 1 or day > days_in_month[month_num]) == (res == "Invalid day")


# Specification 3: Winter season boundaries (Dec 21 - Mar 20)
assert (res == "Winter") == ((month.lower() == "december" and day >= 21) or
                             month.lower() == "january" or
                             month.lower() == "february" or
                             (month.lower() == "march" and day <= 20))

# Specification 4: Spring season boundaries (Mar 21 - Jun 20)
assert (res == "Spring") == ((month.lower() == "march" and day >= 21) or
                             month.lower() == "april" or
                             month.lower() == "may" or
                             (month.lower() == "june" and day <= 20))

# Specification 5: Summer season boundaries (Jun 21 - Sep 20)
assert (res == "Summer") == ((month.lower() == "june" and day >= 21) or
                             month.lower() == "july" or
                             month.lower() == "august" or
                             (month.lower() == "september" and day <= 20))

# Specification 6: Autumn season boundaries (Sep 21 - Dec 20)
assert (res == "Autumn") == ((month.lower() == "september" and day >= 21) or
                             month.lower() == "october" or
                             month.lower() == "november" or
                             (month.lower() == "december" and day <= 20))
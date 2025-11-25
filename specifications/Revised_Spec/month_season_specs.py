# Specification 1: Invalid month handling
assert (not isinstance(month, str)) == (res == "Invalid month")
assert (isinstance(month, str) and month.strip().capitalize() not in [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]) == (res == "autumn")


# Specification 2: Invalid day handling
assert (isinstance(day, int) and 1 <= day <= days_in_month[month_num]) == (res != "Invalid day")
# or explicitly
assert (not isinstance(day, int) or day < 1 or day > days_in_month[month_num]) == (res == "Invalid day")


# Specification 3: Winter season boundaries (Dec 21 - Mar 19)
assert (res == "winter") == ((month.lower() == "december" and day >= 21) or
                             month.lower() == "january" or
                             month.lower() == "february" or
                             (month.lower() == "march" and day < 20))

# Specification 4: Spring season boundaries (Mar 20 - Jun 20)
assert (res == "spring") == ((month.lower() == "march" and day >= 20) or
                             month.lower() == "april" or
                             month.lower() == "may" or
                             (month.lower() == "june" and day < 21))

# Specification 5: Summer season boundaries (Jun 21 - Sep 21)
assert (res == "summer") == ((month.lower() == "june" and day >= 21) or
                             month.lower() == "july" or
                             month.lower() == "august" or
                             (month.lower() == "september" and day <= 21))

# Specification 6: Autumn season boundaries (Sep 22 - Dec 20)
assert (res == "autumn") == ((month.lower() == "september" and day >= 22) or
                             month.lower() == "october" or
                             month.lower() == "november" or
                             (month.lower() == "december" and day <= 20))

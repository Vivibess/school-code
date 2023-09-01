months_and_days = {1: [31, "January"], 2_0: [28, "February"], 2_1: [29, "February"], 3: [31, "March"], 4: [30, "April"], 
                    5: [31, "May"], 6: [30, "June"], 7: [31, "July"], 8: [31, "August"],
                    9: [30, "September"], 10: [31, "October"], 11: [30, "November"], 12: [31, "December"]}

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True

def days_in_month(month, year):
    if month == 2:
        if is_leap_year(year):
            return months_and_days.get(2_1)[0]
        else:
            return months_and_days.get(2_0)[0]
    else:
        return months_and_days.get(month)[0]

while True:
    try:
        month = int(input("Please enter the month as a number.\n"))
        year = int(input("Please enter the year as a number.\n"))
        # Arbitrary range for years
        if month in range(1, 13) and year in range(0,10000):
            break
        else:
            print("Not valid input, please try again.")
    except ValueError:
        print("Please enter the month and year as numbers.")


if month == 2:
    if is_leap_year(year):
        print(months_and_days.get(2_1)[1], year, "has", days_in_month(month, year), "days.")
    else:
        print(months_and_days.get(2_0)[1], year, "has", days_in_month(month, year), "days.")
else:
    print(months_and_days.get(month)[1], year, "has", days_in_month(month, year), "days.")
# Print out a date, given year, month, and day as numbers

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# A list with one ending for each number from 1 to 31
endings = ["st", "nd", "rd"] + 17 * ["th"] + ["st", "nd", "rd"] + 7 * ["th"] + ["st"]

year = raw_input("Year: ")
month = raw_input("Month (1-12): ")
day = raw_input("Day (1-31): ")

# Remember to subtract 1 from month and day to get a correct index
month_name = months[int(month) - 1]
ordinal = day + endings[int(day) - 1]

print(month_name + " " + ordinal + ", " + year)

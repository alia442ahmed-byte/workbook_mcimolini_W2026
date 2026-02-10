days_of_the_week = ["Sunday",
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday"]

weekend_days = ("Saturday", "Sunday") # This is a tuple. It can't be changed once defined or else we get errors.

# for var in list:
print("Days of the week are:")
for day in days_of_the_week:
    if day in weekend_days:
        print(f"{day} is a weekend day!")
    else:
        print(f"{day} is a weekday.")

# enumerate(list) returns the index and the value for each item in the list
for index, day in enumerate(days_of_the_week):
    print(f"{day} is day number {index + 1} of the week.") # using + 1 to make our numbering match our expectations.

# continue is a keyword that tells our loop to move on to the next item. No code after continue runs for that index.
for day in days_of_the_week:
    if "u" in day: # strings are just fancy lists, so we can use for and in on them
        continue
    print(f"{day} does not contain the letter 'u'")

# break is a keyword that tells our loop to end. No loop code runs after break.
for day in days_of_the_week:
    if day == "Wednesday":
        break
    print(f"{day} is before Wednesday.")

# any code after the loop will run after break
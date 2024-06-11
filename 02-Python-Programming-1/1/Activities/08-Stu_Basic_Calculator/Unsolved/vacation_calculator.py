100# Ask the user what their vacation budget is and convert it to a float
budget = float(input("What is your total vacation budget? "))

# Ask the user how much of their budget should be spent on flights and 
# accommodation and convert it to a float
flights_accommodation = float(input("What is your budget for the flights and "
                                    + "accommodation? "))

# Ask the user how much they would like to spend per day and convert it to a float
daily_budget = float(input("What is your preferred daily budget? "))

# Ask the user how many days they will go on vacation and convert it to an
# integer
vacation_days = float(input("How many days will you go on vacation? "))

# Ask the user the currency exchange rate for the country they're visiting and
# convert it to a float
exchange_rate = float(input("What is the currency exchange rate? "))

# Ask the user for the radius distance they're willing to walk from their
# hotel and convert it to a float
distance = float(input("What is the radius distance you're willing to walk "
                       + "from your hotel (in meters)? "))

# Calculate the budget remaining after flights and accommodation
budget_remaining = budget - flights_accommodation
print(budget_remaining)
# Calculate the remaining budget in local currency amount
budget_remaining_local = budget_remaining * exchange_rate
print(budget_remaining_local)
# Calculate the budget per day in the local currency
budget_per_day_local = daily_budget * exchange_rate
print(budget_per_day_local)
# Calculate the budget per day in the local currency, ignoring cents
budget_per_day_local_int = int(budget_per_day_local)
print(budget_per_day_local_int)
# Calculate the total area around the hotel the user can walk within
# Area of a circle = pi * radius ** 2
pi = 3.14159265358979323846
total_area = pi * (distance ** 2) 
print(total_area)
# Calculate the amount left from the budget if the user sticks with their
# daily budget. This is a modulus problem.
amount_leftover = budget_remaining - (daily_budget * vacation_days)
print(amount_leftover)

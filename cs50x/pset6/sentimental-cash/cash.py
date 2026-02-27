from cs50 import get_float

# Ask for change
while True:
    change = get_float("Change: ")
    if change > 0:
        break

# Convert dollars to cents
change = round(change * 100)

# Count
coins = 0

# Assign coins value
quarter = 25
dime = 10
nickel = 5
penny = 1

coins += change // 25  # divide change by quarter (25), add the result to coins
change %= 25         # use mod quarter (25) to calculte the remaining change

coins += change // 10  # repeat the process, divide with 10
change %= 10          # remaining change

coins += change // 5  # repeat the process, divide with 5
change %= 5          # remaining change

coins += change // 1  # no need to use mod because the rest is now 0

print(coins)

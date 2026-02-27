from cs50 import get_int

# Ask for integer between 1 and 8
while True:
    n = get_int("Height: ")
    if n >= 1 and n <= 8:
        break

# Print the pyramid
for i in range(1, n + 1):
    print(" " * (n - i) + "#" * i + "  " + "#" * i)

input = input("Expression: ").strip()

x, y, z = input.split(" ")
x = float(x)
z = float(z)

if y == '+':
    print(round((x + z), 1))
if y == '-':
    print(round((x - z), 1))
if y == '*':
    print(round((x * z), 1))
if y == '/':
    print(round((x / z), 1))

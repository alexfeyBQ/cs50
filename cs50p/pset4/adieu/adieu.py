import inflect
p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ").title()
        if name not in names:
            names.append(name)
    except EOFError:
        print("\n")
        break

print("Adieu, adieu, to", p.join(names[0:]))

input = input("camelCase: ")

print("snake_case: ", end='')
for c in input:
    if c.isupper():
        print('_' + c.lower(), end='')
    else:
        print(c.lower(), end='')
print("")

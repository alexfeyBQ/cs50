input = input("Input: ")

for c in input:
    if c.lower() != 'a' and c.lower() != 'e' and c.lower() != 'i' and c.lower() != 'o' and c.lower() != 'u':
        print(c, end='')

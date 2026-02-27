input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().title()

if input == "42" or input == "Forty Two" or input.lower() == "forty-two":
    print("Yes")
else:
    print("No")

from random import randint

def main():
    level = get_level()
    score = 0

    for i in range(10):
        counter = 0
        x = generate_integer(level)
        y = generate_integer(level)

        while True:
            answer = x + y

            try:
                guess = int(input(f"{x} + {y} = "))

            except ValueError:
                counter, limit = error(x, y, answer, counter)
                if limit:
                    break
                continue

            if guess == answer:
                score += 1
                break
            else:
                counter, limit = error(x, y, answer, counter)
                if limit:
                    break

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2 , 3]:
                break

        except ValueError:
            pass

    return level

def generate_integer(level):
    if level == 1: k, n = 0, 9
    if level == 2: k, n = 10, 99y
    if level == 3: k, n = 100, 999

    return randint(k, n)

def error(x, y, answer, counter):
    print("EEE")
    counter += 1

    if counter == 3:
        print(f"{x} + {y} = {answer}")
        return counter, True

    return counter, False

if __name__ == "__main__":
    main()

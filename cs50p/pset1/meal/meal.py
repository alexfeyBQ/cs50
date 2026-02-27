def main(input):
    t = convert(input)

    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

def convert(time):
    h, min = time.split(':')
    h = float(h)
    min = float(min)
    t = h + (min / 60)
    return t

if __name__ == "__main__":
    input = input("What time is it? ")
    main(input)

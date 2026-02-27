while True:
    try:
        frac = input("Fraction: ").split('/')
        X = int(frac[0])
        Y = int(frac[1])

        if X > Y or X < 0 or Y <= 0:
            continue

        result = round((X / Y) * 100)

        if result <= 1:
            print('E')
        elif result >= 99:
            print('F')
        else:
            print(f"{result}%")
        break

    except (ValueError, ZeroDivisionError):
        pass




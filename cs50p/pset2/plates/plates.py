def main():
    plate = input("Plate: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    forbidden = ['.', '?', '!', ' ', ',', ':', "'", ';', '"', '-']
    start = False
    if len(s) <= 6 and len(s) >= 2 and s[0:2].isalpha():
        for c in s:
            if c in forbidden:
                return False
            elif c.isdigit():
                if not start:
                    if c == '0':
                        return False
                    start = True
            elif start:
                return False
        return True
    else:
        return False

main()

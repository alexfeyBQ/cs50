from random import randint

while True:
    try:
        N = int(input("Level: "))
        if N >= 1:
            n = randint(1, N)
            break
        
    except ValueError:
        pass

while True:
    try:
        guess = int(input("Guess: "))

        if guess < 1:
            continue
        elif guess == n:
            print("Just right!")
            break
        elif guess > n:
            print("Too large!")
        else:
            print("Too small!")

    except ValueError:
        pass

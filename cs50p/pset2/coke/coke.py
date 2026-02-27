print("Amount Due: 50")
due = 50

while due > 0:
    coin = int(input("Insert Coin: "))
    coins = [5, 10, 25]

    if coin in coins:
        due -= coin
        if due > 0:
            print(f"Amount Due: {due}")
    else:
        print(f"Amount Due: {due}")

print(f"Change Owed: {-due}")

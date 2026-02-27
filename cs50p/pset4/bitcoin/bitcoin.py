import sys
import requests

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)
else:
    try:
        n = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    try:
        response = requests.get("https://api.coincap.io/v3/assets/bitcoin?apiKey=e6aee420c32815932c472a20f52b8eba05bad087422971752c9d1008514e0636")
        data = response.json()

    except requests.RequestException:
        print("Couldn't retrieve data.")
        sys.exit(1)

    amount = n * float(data["data"]["priceUsd"])
    print(f"${amount:,.4f}")



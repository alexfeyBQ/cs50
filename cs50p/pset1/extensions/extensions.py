input = input("File name: ").strip().lower()

if input.endswith('.jpg') or input.endswith('.jpeg'):
    print("image/jpeg", end="")
elif input.endswith('.gif'):
    print("image/gif", end="")
elif input.endswith('.png'):
    print("image/png", end="")
elif input.endswith('.pdf'):
    print("application/pdf", end="")
elif input.endswith('.txt'):
    print("text/plain", end="")
elif input.endswith('.zip'):
    print("application/zip", end="")
else:
    print("application/octet-stream", end="")

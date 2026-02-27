import sys
from pyfiglet import Figlet

if len(sys.argv) == 1:
    format = Figlet()
elif len(sys.argv) == 3 and sys.argv[1] == "-f":
    format = Figlet(font=sys.argv[2])
else:
    sys.exit(1)

text = input("Input: ")
print("Output: ")
print(format.renderText(text))

from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 3:
  if sys.argv[1] != "-f" and sys.argv[1] != "--font":
    sys.exit("fuck off!")
  else:
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(input("Input: ")))

elif len(sys.argv) == 1:
  random_font = random.choice(figlet.getFonts())
  figlet.setFont(font=random_font)
  print(figlet.renderText(input("Input: ")))

else:
  sys.exit("provide proper format !!")







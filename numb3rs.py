
import re
import sys

def main():
  print(validate(input("IPV4 Address: ")))

def validate(ip):
   if re.search(r"^(([0-9]?[0-9])|([0-2][0-2][0-5]))\.(([0-9]?[0-9])|([0-2][0-2][0-5]))\.(([0-9]?[0-9])|([0-2][0-2][0-5]))\.(([0-9]?[0-9])|([0-2][0-2][0-5]))$", ip):
     return True
   else:
     return False
     





if __name__ == "__main__":
  main()

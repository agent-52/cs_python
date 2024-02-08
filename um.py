
import re

def main():
  print(count(input("Text: ")))

def count(s):
  s = s.lower()
  ums = re.findall(r"\bum\b", s)
  
  return len(ums)
  





if __name__ == "__main__":
  main()
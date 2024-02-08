import re

def main():
  print(parse(input("HTML: ")))


def parse(s):
  if "src" in s:
    print("yes")
    match = re.search(r'src=("\S*")', s)
    return match.group(1)

  else:
    return None



if __name__ == "__main__":
  main()
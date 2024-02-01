def main():
  time = input("What time is it? ")
  if convert(time) >= 7.0 and convert(time) <= 8.0 :
    print("breakfast time")

def convert(n):
  first, second = n.split(":")
  x = float(first)
  y = float(second)/60
  total_time = x+y
  return total_time

main()



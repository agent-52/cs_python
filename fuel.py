def main():
  percentage = get_percentage() 
  if percentage <= 1:
    print("E")
  elif percentage >= 99:
    print("F")
  else:
    print(f"{percentage}%")
  

  


def get_percentage():
  while True:
    fraction = input("Fraction: ")
    first, second = fraction.split("/")

    try:
      first = int(first)
      second = int(second)
      return round((first/second)*100)
    except ValueError:
      pass
    except ZeroDivisionError:
      pass


main()
      
  

  

  







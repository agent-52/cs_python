import random


def main():
  level = get_level()
  correct_count = 0
  for _ in range(10):
    x = generate_integer(level)
    y = generate_integer(level)
    answer = x + y
    eee_count = 0
    
    
    while True:
      try:
        answer_guess = int(input(f"{x} + {y} = "))
      except ValueError:
        print("EEE")
        eee_count += 1
        if eee_count == 3:
         print(answer)
         correct_count = correct_count - 1 
         break
      else:
        if answer_guess != answer:
          print("EEE")
          eee_count += 1
          if eee_count == 3:
            print(answer)
            correct_count = correct_count - 1  
            break
        else:
          break
    correct_count += 1

  print(f"Your Score: {correct_count}/10")
    
    
    
         
    

    
            



def get_level():
  while True:
      try:
          level = int(input("Level: "))
      except ValueError:
          pass
      else:
          if 1<=level<=3:
              return level
          


def generate_integer(level):
  if level == 1:
     return random.randint(0, 9)
  elif level == 2:
     return random.randint(10, 99)
  elif level == 3:
     return random.randint(100, 999)
  else:
     raise ValueError
  


if __name__ == "__main__":
    main()
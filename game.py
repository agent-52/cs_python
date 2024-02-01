import random

def main():
  level = get_level()
  user_guess = get_user_guess()
  pc_guess = random.randint(1, level)

  if user_guess < pc_guess:
    print("Too small!")
  elif user_guess > pc_guess:
    print("Too large!")
  else:
    print("Just right!")



def get_level():
  while True:
    try:
      level = int(input("Level: "))
    except ValueError:
      pass
    else:
      if level >= 1:
        return level
      
def get_user_guess():
  while True:
    try:
      user_guess = int(input("Guess: "))
    except ValueError:
      pass
    else:
      if user_guess >= 1:
        return user_guess
  
      
main()





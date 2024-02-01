def main():
  statement = input("Input: ").lower()
  remove_vowel(statement)

def remove_vowel(x):
  vowels = ["a", "e", "i", "o", "u"]
  for letter in x:
    for vowel in vowels:
      if letter == vowel:
        x = x.replace(letter, "")
  print(x)
    
  

main()
def main():
  camelCase = input("camelCase: ")
  snake_case(camelCase)

def snake_case(sentence):
  letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

  i = 0

  while i < 100:
    for letter in letters:
      x = sentence.find(letter)
      if x != -1:
        sentence = sentence[:x] + "_" + sentence[x].lower() + sentence[x+1:]
    i += 1
      
  
  
  print("snake_case: " + sentence)
    
    
main()
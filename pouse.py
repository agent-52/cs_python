answer = input("What is the answer to the great question of life ").lower()

match answer:
  case "42" | "forty-two" | "forty two":
    print("yes")
  case _ :
    print("No")
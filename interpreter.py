expression = input("Expression: ")
x, operator, z = expression.split(" ")

first_operand = float(x)
second_operand = float(z)


if operator == "+":
  result = first_operand + second_operand
  print(result)
elif operator == "-":
  result = first_operand - second_operand
  print(result)
elif operator == "*":
  result = first_operand * second_operand
  print(result)
elif operator == "/":
  result = first_operand/second_operand
  print(result)

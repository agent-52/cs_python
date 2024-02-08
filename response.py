import validators
email = input("Email: ")
if validators.email(email):
  print("valid")
else:
  print("invalid")


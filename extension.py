file_name = input("Enter file name ").lower()
first, last = file_name.split(".")

if last == "gif" or "jpg" or "jpeg" or "png" :
  print("image")
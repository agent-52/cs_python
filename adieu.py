

name = ""
while True:

  try:
    name = name+ " "+ input("Name: ").strip()
  except EOFError:
    break
  
list = name.split(" ")[1:]

if len(list) == 2:
  last_name = list[-1]
  second_last_name = list[-2]
  

  print("Adieu, adieu, to " +second_last_name+ " and "+ last_name)

elif len(list) > 2:
  last_name = list[-1]

  name_list2 = ""
  for i in range(len(list)-1):
    name_list2 += list[i]+", "

  print("Adieu, adieu, to " +name_list2+"and "+ last_name)
  
else:
  print("Adieu, adieu, to " +list[0])








  
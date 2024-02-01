
list = []
count = 0
name_list = []

while True:
  try:
    item = input().upper()
  except EOFError:
    break
  else:
    list.append(dict({"name": item, "count": count}))
    name_list.append(item)

for subject in list:
  for name in name_list:
    if subject["name"] == name:
      subject["count"] += 1


for subject in list:
  print(subject["count"], subject["name"])


    


  








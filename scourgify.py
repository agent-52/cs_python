import csv
import sys

if len(sys.argv) <3:
  sys.exit("too few arguments")
elif len(sys.argv) >3:
  sys.exit("too many arguments")

old_file = sys.argv[1]
new_file = sys.argv[2]

try:
  file = open(old_file)
except FileNotFoundError:
  sys.exit("cant oprn this file")

unordered_file = []
with open(old_file) as file:
  reader = csv.DictReader(file)
  for row in reader:
    unordered_file.append(row)

with open(new_file, "a") as new_file:
  writer = csv.DictWriter(new_file, fieldnames=["first", "last", "house"])
  for item in unordered_file:
    last, first = item["name"].split(",")
    house = item["house"]
    writer.writerow({"first": first, "last": last, "house": house})
  
  





    
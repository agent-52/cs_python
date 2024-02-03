import sys
from tabulate import tabulate
import csv

if len(sys.argv) != 2:
  sys.exit("one argument is allowed")

file_name = sys.argv[1]
if file_name[-4: ] != ".csv":
  sys.exit("Not a csv file")

try:
  file = open(sys.argv[1])
except FileNotFoundError:
  sys.exit("file not found")

items = []

with open(file_name) as file:
  reader = csv.reader(file)
  for row in reader:
    items.append(row)



print(tabulate(items, tablefmt="grid"))
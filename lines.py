import sys

if len(sys.argv) != 2:
  sys.exit("only one argument is allowed")

file_name = sys.argv[1]
if file_name[-3: ] != ".py":
  sys.exit("Not a Python file")

lines = []
line_count = 0

try:
  file = open(file_name)
except FileNotFoundError:
  sys.exit("File does not exist")

with open(file_name) as file:
  for line in file:
    lines.append(line.rstrip())

for line in lines:
  line = line.strip()
  if line.startswith("#") == False and line != "":
    line_count += 1

print(line_count)




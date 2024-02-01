
month_list = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December"
]

def main():
  while True:
    date = input("Date: ")
    if date1(date) == True:
      print(convert_date1(date))
      break
    elif date2(date) == True:
      print(convert_date2(date))
      break
    else:
      continue


def date1(date):
  try:
    month, date, year = date.split("/")
    month = int(month)
    date = int(date)
    year = int(year)
  except ValueError:
    return False
  else:
    if 0<= month <= 12 and 1<= date <= 31 and year > 0:
      return True
    else:
      return False
    
def date2(date):
  try:
    month_date, year = date.split(",")
    year = int(year)
    month, date = month_date.split(" ")
    date = int(date)
    month = month.capitalize()
  except ValueError:
    return False
  else:
    for i in range(12):
      if month_list[i] == month:
        if 0<= i <= 12 and 1<= date <= 31 and year > 0:
          return True
        else:
          return False



def convert_date1(date): 
  try:
    month, date, year = date.split("/")
    month = int(month)
    date = int(date)
    year = int(year)
  except ValueError:
    pass
  else:
    if 0<= month <= 12 and 1<= date <= 31 and year > 0:
      if month <= 9:
        month = "0"+str(month)
      if date <= 9:
        date = "0"+str(date)
      
      return f"{year}-{month}-{date}"
    
      
def convert_date2(date):
  try:
    month_date, year = date.split(",")
    year = int(year)
    month, date = month_date.split(" ")
    date = int(date)
    month = month.capitalize()
  except ValueError:
    pass
  else:
    for i in range(12):
      if month_list[i] == month:
        if 0<= i <= 12 and 1<= date <= 31 and year > 0:
          return f"{year}-{i+1:02}-{date:02}"



      

main() 





  

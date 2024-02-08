import re

def main():
  print(convert(input("Hours: ")))


def convert(str):
  if zone := re.fullmatch(r"([0-9][0-9]?):([0-9]{2}) (AM|PM) to ([0-9][0-9]?):([0-9]{2}) (AM|PM)", str):
    zone1 = zone.group(3)
    zone2 = zone.group(6)
    time1 = int(zone.group(1))
    time2 = int(zone.group(4))
    if zone1 == "PM":
      time1 = time1+12
    if zone2 == "PM":
      time2= time2+12

    return f"{time1:02}:{zone.group(2)} to {time2:02}:{zone.group(5)}"
  
    


  elif zone:= re.fullmatch(r"([0-9][0-9]?) (AM|PM) to ([0-9][0-9]?) (AM|PM)", str):
    zone1 = zone.group(2)
    zone2 = zone.group(4)
    time1 = int(zone.group(1))
    time2 = int(zone.group(3))
    if zone1 == "PM":
      time1 = time1+12
    if zone2 == "PM":
      time2= time2+12

    return f"{time1:02}:00 to {time2:02}:00 {zone2}"

    

  else:
    return ValueError
  

if __name__ == "__main__":
  main()

import random
year=random.randint(1993,2018)
print(year)
if(year%4==0 and year%100!=0 or year%400==0):
  print("leap year")
else:
  print("normal year")
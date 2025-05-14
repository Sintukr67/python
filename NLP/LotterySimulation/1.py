import random
#bet=int(input("your bet from 1 to 10:"))
account=0
for i in range(7):
  bet=random.randint(1,10)
  lucky_draw=random.randint(1,10)
  print(lucky_draw)
#account=0
  if bet==lucky_draw:
    account=account+900-100
  else:
    account=account-100

  print(account)
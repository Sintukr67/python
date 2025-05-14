import random
import matplotlib.pyplot as plt
#bet=int(input("your bet from 1 to 10:"))
account=0
x=[]
y=[]

for i in range(365):
    x.append(i+1)
    bet=random.randint(1,10)
    lucky_draw=random.randint(1,10)
  # print(lucky_draw)
#account=0
    if bet==lucky_draw:
      account=account+900-100
    else:
      account=account-100
    y.append(account)  

print("Amount in your game account" , account)
plt.plot(x,y)
plt.show()
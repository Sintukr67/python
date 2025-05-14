def fact(n):
  #base case
  if n==0:
    return 1
  else:
    return n * fact(n-1)
  
n=int(input("enter the number:"))
if n<0:
  print('factorial is not defined on negative number') 
else:
  f=fact(n)
  print("factorial of",n,'is',f)   
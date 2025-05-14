for i in range(1,51):
  if(i%3==0 and i%5==0):
    print(str(i)+"fizzBuzz")
    #print(str(i)+"fizz")
  else:
    if(i%5==0):
      print(str(i)+"buzz")
    else:
      if(i%3==0):
        print(str(i)+"fizz")
      else:
        print(i)
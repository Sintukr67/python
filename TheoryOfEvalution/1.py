#writing to a file
with open("myfile.txt","w") as f:
    f.write("this is the first line of code")
    f.write("this is the second line of code")
    print("the above file is created successfully")
    
  #read from a file
    with open("example.txt","r") as f:
      content=f.read()
    print("this file you can read.\n")
    


    

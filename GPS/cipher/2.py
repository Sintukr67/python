import string 
dict={}
data=""
file=open("op_file.txt","w")
for i in range(len(string.ascii_letters)):
  dict[string.ascii_letters]=string.ascii_letters[i-1]
print(dict)
with open("ip_file.txt") as f:
  while True:
    c=f.read(1)#we have give here some bit value to read 
    if not c:
      print("End of file")
      break
    if c in dict:#checking the character weather it end or not
      data=dict[c]
    else:
      data=c
    file.write(data)  
    print(data)
file.close()       

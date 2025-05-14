def rock_paper_scissor(nums1,nums2,bit1,bit2):
  p1=int(num1[bit1])%3
  p2=int(num2[bit2])%3
  if(player1[p1]==player2[p2]):
   print("player1 won!!")
  elif(player1[p1]=="Rock" and player2[p2]=="Scissor"):
    print("player1 won!!")
  elif(player1[p1]=="Paper" and player2[p2]=="Rock"):
    print("player1 won!!")
  elif(player1[p1]=="Scissor" and player2[p2]=="Paper"):
    print("player1 won!!")
  else:
    print("player2 won!!")         



player1={0:'Rock',1:'Paper',2:'Scissor'}
player2={0:'Rock',1:'Paper',2:'Scissor'}
while(1):
  num1=input("player1,Enter your choice:")#enter any digit number like 3456778

  num2=input("player2,Enter your choice:")
  #enter any digit number like 3456778899
  bit1=int(input("player1,Enter the secret bit position:"))#pos should up to length of num
  
  bit2=int(input("player2,Enter the secret bit position:"))
  
  #call a function
  rock_paper_scissor(num1,num2,bit1,bit2)
  #to stop when we dont want to play
  ch=input("Do you want to continue? y/n")
  if(ch=='n'):
    break

#step-1
import numpy
board=numpy.array([['_','_','_'],['_','_','_'],['_','_','_']])
p1s='X'
p2s='O'

def check_row(symbol):
  for r in range(3):
    count=0
    for c in range(3):
      if board[r][c]==symbol:
        count=count+1
    if count==3:
      print(symbol,'won')
      return True
  return False

def check_col(symbol):
  for c in range(3):
    count=0
    for r in range(3):
      if board[r][c]==symbol:
        count=count+1
    if count==3:
      print(symbol,'won')
      return True         
  return False

def check_dia(symbol):
  if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
    print(symbol,'won')
    return True
  if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
    print(symbol,'won')
    return True
  return False



def won(symbol):
  return check_row(symbol) or check_col(symbol) or check_dia(symbol)



def place(symbol):
  while(1):   
      row=int(input('Enter row (0-2): '))
      col=int(input('Enter column (0-2): '))
      if board[row][col]=='_':
          break
      else:
        print("Invalid input,Please enter again")
  board[row][col]=symbol
    
#step-3
def play():
  for turn in range(9):
    if turn%2==0:
      print('X turn')
      place(p1s) #fun call for place symbol
      if won(p1s): #fun call for check winning condition
        break
    else:
      print('O turn')
      place(p2s)
      if won(p2s):
        break 
  #after filling board if no one won then it will draw      
  if not (won(p1s)) and not (won(p2s)):
    print("Game is draw") 
#step-2    
play()   #fun call   
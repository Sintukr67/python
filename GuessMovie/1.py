
import random
movie=["anand","drishyam","anbe shivam","gol maal","khosla ka ghosla","3 idiots","dil chahta hai","zindagi na milegi dobara","queen","pyaar ka punchnama"]
def create_question(movie):
  n=len(movie)
  letters=list(movie)
  temp=[]
  for i in range(n):
    if letters[i]==' ':
      temp.append(' ')
    else:
      temp.append('*')
  qn=''.join(str(x) for x in temp)
  return qn      
def is_present(letter,movie):
  c=movie.count(letter)
  if c==0:
    return False
  else:
    return True
  
def unlock(qn,movie,letter):
  ref=list(movie)
  qn_list=list(qn)
  temp=[]
  n=len(movie)
  for i in range(n):
    if ref[i]==' ' or ref[i]==letter:
      temp.append(ref[i])
    else:
      if qn_list[i]=='*':
        temp.append('*')
      else:
        temp.append(ref[i])
  qn_new=''.join(str(x) for x in temp)
  return qn_new


def play():
  player1=input("player1 enter your name:")
  player2=input("player2 enter your name:")
  pp1=0
  pp2=0
  turn=0
  willing=True
  while willing:
    if turn%2==0:
      #player1's turn
      print("player1's turn")
      picked_movie=random.choice(movie)
      qn=create_question(picked_movie)
      print(qn)
      modified_qn=qn

      not_said=True
      while not_said:
        letter=input("your letter:")
        if(is_present(letter,picked_movie)):
          #unlock:
          modified_qn=unlock(modified_qn,picked_movie,ch)
          print(modified_qn)
          dission=input("press 1 to guess the movie or 2 to unlock another letter:")
          if dission==1:
            ans=input("your answer:")
            if ans==picked_movie:
              pp1=pp1+1
              print("correct")
              not_said=False
              print(player1,"your score is: ",pp1)
          else:
            print("wrong answer. Try again.")



        else:
          print(letter,"not found")
      c=input("press 1 to continue or 0 to quit:")
      if c==0:
        willing=False
        print(player1,"your score is:", pp1)
        print(player2,"your score is:", pp2)
        if pp1>pp2:
          print(player1,"won")
        elif pp2>pp1:
          print(player2,"won")
        else:
          print("match draw")
          print("thank you for playing")
          break
    else:
      #player2's turn
      print("player2's turn")
      picked_movie=random.choice(movie)
      qn=create_question(picked_movie)
      print(qn)
      modified_qn=qn

      not_said=True
      while not_said:
        letter=input("your letter:")
        if(is_present(letter,picked_movie)):
          #unlock:
          modified_qn=unlock(modified_qn,picked_movie,ch)
          print(modified_qn)
          dission=input("press 1 to guess the movie or 2 to unlock another letter:")
          if dission==1:
            ans=input("your answer:")
            if ans==picked_movie:
              pp2=pp2+1
              print("correct")
              not_said=False
              print(player2,"your score is: ",pp2)
          else:
            print("wrong answer. Try again.")



        else:
          print(letter,"not found")
      c=input("press 1 to continue or 0 to quit:")
      if c==0:
        willing=False
        print(player1,"your score is:", pp1)
        print(player2,"your score is:",pp2)
        if pp1>pp2:
          print(player1,"won")
        elif pp2>pp1:
          print(player2,"won")
        else:
          print("match draw")
          print("thank you for playing")
          break
    turn=turn+1      


play()  
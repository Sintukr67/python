import turtle

turtle.bgcolor("black")
seurat=turtle.Turtle()

width=5
height=7
dot_distance=25
seurat.setpos(-250,250)







def spiral(m,n):
  r=0
  c=0
  f=0
  seurat.color("white")

  while(r<m and c<n):
    if f==1:
      seurat.right(90)
    #printing the first row from the remaining rows
    for j in range(c,n):
      #print(a[r][j], end=" ")
      seurat.forward(dot_distance)

    r+=1
    f=1

    seurat.right(90)
    #printing the last column from the remaining columns
    for i in range(r,m):
      #print(a[i][n-1], end=" ")
      seurat.forward(dot_distance)

    n-=1
    seurat.right(90)

    if r<m:
      #printing the last row
      for j in range(n-1,c-1,-1):
#print(a[m-1][j], end=" ")
        seurat.forward(dot_distance)
      
      m-=1
    seurat.right(90)  

    if c<n:
        #printing the first column from the remaining columns
        for i in range(m-1,r-1,-1):
         # print(a[i][c], end=" ")
         seurat.forward(dot_distance)
        c+=1





# a=[]
# count=1
# for i in range(4):
#   l=[]
#   for j in range(4):
#     l.append(count)
#     count+=1
#   a.append(l)
spiral(20,20)


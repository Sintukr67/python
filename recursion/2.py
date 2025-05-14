def binary_search(l,x,start,end):
  #base case
  if start==end:
    if l[start]==x:
      return start
    else:
      return -1


  mid=int((start+end)/2)
  if l[mid]==x:
    return mid
  elif l[mid]>x:
    return binary_search(l,x,start,mid-1)
  else:
    return binary_search(l,x,mid+1,end)
  




l=[12,5,3, 7, 8, 9, 10]
l.sort()
x=int(input("Enter a key:"))
index=binary_search(l,x,0,len(l)-1)
if(index==-1):
  print(x,"is not found")
else:
  print(x,"is found at index:",index+1)

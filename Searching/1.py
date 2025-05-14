# arr=[10,30,50,5,33,67]
# target=33
# found=False
# for i in range(len(arr)):
#   if arr[i]==target:
#     print(f"{target} found at index {i}")
#     found=True
#     break

# if not found:
#   print(f"{target} not found in the arr.")


def binary_search(arr,target):
  # left=0,right=len(arr)-1
  left,right=0,len(arr)-1
  while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
      return mid
    elif(arr[mid]<target):
      left=mid+1
    else:
     right=mid+1
  return -1    
      



#example
arr=[10,30,50,55,63,67]
target=63
result=binary_search(arr,target)

if result !=-1:
  print(f"{target} found at index {result}")

else:
  print(f"{target} not found")  

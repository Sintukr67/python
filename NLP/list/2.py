# t1="ram"
# t2="shyam"
# t3="sita"
# i="sudershan"

# #list

shopping=["milk","bread","eggs","butter"]
# print(shopping)

# for i in range(3):
#   print(i)
  
  
  

# for item in shopping:
#     print(item)



#append -added to the end

shopping.append("curd")
for item in shopping:
   print(item)

#remove - remove the first occurrence of the item
print(shopping)
shopping.remove("milk")

print(shopping)

#insert - insert at a specific index
shopping.insert(1,"halwa")
print(shopping)

ages=[12,34,50,44,32,59,8,25,22,19,10]
print(ages.count(44))

for item  in ages:
   if(item>=20):
    print(item)


print(len(ages)) 

ages.sort()

print(ages)

ages.reverse()
print(ages)

#slicing
#list name[start:end+1]
#list_name[start_index:end_index+1]
students=["rohan","sunny","sintu","raushan","mayank"]
students.sort()

print(students)

print(students[1:3])
print(students[:3])#default start 0
print(students[1:])#default end lenth of list

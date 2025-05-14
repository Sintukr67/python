str1=input("Enter the first string:")
str2=input("Enter the second string:")

print(sorted(str1))
print(sorted(str2))
if str1==str2:
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
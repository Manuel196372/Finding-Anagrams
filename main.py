# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


str1 = input("string1:")
str2 = input("string2:")

sortedStr1 =  sorted(str1)
sortedStr2 =  sorted(str2)

if sortedStr1 == sortedStr2:
    print("True")
else:
    print("False")

    
 

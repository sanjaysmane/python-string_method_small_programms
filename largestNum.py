  
#take input from the user
value1 = int(input("Enter number: "))
value2 = int(input("Enter number: "))
value3 = int(input("Enter number: ")) 

if (value1 >value2) and (value1 > value3):
  print("largest = ", value1)
elif (value2 > value1) and (value2 > value3):
  print("largest = ", value2)
else:
  print("largest = ", value3)
  

  
# asking number of elements to put in list 

num = int(input("Enter number of elements in list: "))
list1 = []
# iterating till num(n), to append numbers in list & to find largest in list.Enter one number at a time.
for i in range(1, num + 1):
  ele = int(input("Enter numbers: "))
  list1.append(ele)
print("Largest number is:", max(list1))
  
  
 
maximum = int(input(" Please Enter up to which sum is to be done : "))
total = 0
 
for number in range(1, maximum+1):
    if(number % 2 == 0):
        print("{0}".format(number))
        total = total + number
 
print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, total))

  
maximum = int(input(" Please Enter up to which sum is to be done : "))
Oddtotal = 0
 
for number in range(1, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number
 
print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, Oddtotal)) 

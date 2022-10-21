


#n = int(input('Enter number up to which sum is to be done: '))
#sum = n
#while n > 0:
    #sum = sum + (n-1)
    #n = (n-1)
#print(sum)   

num = int(input('Enter number up to which sum is to be done: '))
a = num
if a < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(a > 0):
       sum += a
       a -= 1
   print("The sum up to entered number {0} is {1}".format(num, sum))
        
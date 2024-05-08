def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
x = int(input("Enter 1st value : "))
y = int(input("Enter 2ed value : "))
print(compute_lcm(x,y))
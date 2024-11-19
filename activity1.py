#Write a program to perform the following operations:
 #1. Create a tuple with different datatypes
  #2. Create another tuple of integers 
#3. Create a new tuple by adding 9 to the previous tuple 
#4. Count the occurrences of an element in the tuple 
#5. Perform slicing on the tuple
tup1=("Codingal",True,45,59)
print("Tuple 1 is : ",tup1)
tup2=(409,95,48,94,22,11)
print("Tuple 2 is : ",tup2)
tup3=tup2+(9,)
print("Tuple 3 is : ",tup3)
tup4=(87,95,9,87,12,23,22,48,95,22,95)
print("Tuple 4 is : ",tup4)
print("Occurence of 95 is : ",tup4.count(95))
print(tup4[1:6])
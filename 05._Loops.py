# WHILE LOOP : ~
count = 1
while count <= 5:
    print("hello")
    count += 1

print(count)

i=1
while i <= 10:
    print("hii" , i)
    i += 1
print(i)

#print number from 1 to 5
p=1
while p<= 5:
    print(p)
    p += 1
print(p)
print(" loop ended")

#to print 1 to 5
q = 5
while q >= 1 :
    print(q)
    q -= 1

print("loop ended")

# questions :
# 1. print numbers from 1 to 100
i=1
while i <= 100: # stopping condition
    print(i)
    i += 1

#2. print numbers from 100 to 1.
i = 100
while i >= 1 :
    print(i)
    i -= 1

#3. print multiplication table of a number n 
n = int(input( " enter number"))
i = 1
while i <= 10:
    print(n*i)
    i += 1

#print elements of the following list using a loop
# [ 1,4,9,16,25,36,49,64,81,100]
i = 1
while i <= 10 :
    print(i**2)
    i += 1
#OR
# traverse
nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums):
    print(idx)
    idx += 1

#search for a number x in this tuple using loop :
#1,4,9,16,25,36,49,64,81,100)
nums = (1,4,9,16,25,36,49,64,81,100,36)
x = 36
i = 0
while i < len (nums):
    if (nums[i] == x):
        print("FOUND ai idx , i")
    else:
        print("finding...")

    i += 1
# BREAK AND CONTINUE : ~
i = 1
while i <= 5:
    print(i)
    if (i==3):
        break
    i += 1

print ("end of loop")

nums = (1,4,9,16,25,36,49,64,81,100,36)


x = 36


i = 0
while i < len (nums):
    if (nums[i] == x):
        print("FOUND ai idx", i)
        break
    else:
        print("finding...")

    i += 1
print( "end of th loop")


i = 0
while i <= 5 :
    if (i == 3):
        i += 1
        continue # skip
    print (i)
    i += 1

#for lopp : ~
# loops are used for sequential traversal. For travelling list, string,tuples etc.

nums = [1,2,3,4]

for val in nums:
    print(val)

veggies = [ "potato" , "brinjal" , "tamato"]

for nam in veggies :
    print(nam)


tup = (1,2,3,4,5)

for num in tup :
    print(tup)

# when we have to work on iterator , we are ubtating and have a stopping conditional in a variable  we use while loop.
# if we want to treverse(travel) on any data type we use for loop.

str = "python loops"

for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)
else:
    print("END") # so,in this way we use else in loopm if we want to run something after complition of whole loop we write that in else.


#print elements of the following list using a loop
# [ 1,4,9,16,25,36,49,64,81,100] by for loop

list = [ 1,4,9,16,25,36,49,64,81,100]

for lis in list :
    print(lis)

#search for a number x in this tuple using loop :
#1,4,9,16,25,36,49,64,81,100)

tuple = (1,4,9,16,25,36,49,64,81,100,16)
x= 16

idx = 0
for el in tuple :
    if (el == x):
        print ("found x at idx " ,idx)
    idx +=1


#RANGE : ~~ # starting value , ending value, step size
#RANGE FUNCTIOMN RETURNS A SEQUENCE OF NUMBERS , STARTING FROM 0 BY DEFAULT AND INCREASING BY 1Q( DEAFAULT) ,
# AND STOPS BEFORE A SPECIFIC NUMBER.
seq = range(5)
print(seq[0]) 
print(seq[1])
print(seq[2])


for i in range(10):
    print(i)

for i in range (4): # range (stop)
    print(i)

for i in range (2,5):
    print(i)

for i in range(2,101,2): # even numbers
    print(i)

#PRACTICE QUESTIONS : ~~
# 1. PRINT NUMBERS FROM 1 TO 100
for i in range(1,101,1):
    print (i)

# 2. print numbers from 100 to 1.
for i in range(100,0,-1):
    print(i)

# 3. print the multiplication table of a number n.
n=int(input("enter a number : "))
for i in range (11) :
    print(i*n)

#PASS STATEMENT :
#pass is a null statement thst does nothing . it is used as a placeholder for future code.

for i in range(5):
   pass # skip (null statement that des nothing)


print("some usefull work after pass")

#PRACTICE QUESTIONS :~~
# 1. WAP to finnd the summ of first n  natural numbers. (using while)
n = 5

sum=  0
for i in range(1, n+1):
    
    sum += i
print( "total sum :" , sum)

n =7
sum =0
i=1
while i<=n:
    sum += i
    i +=1
print ("total sum" , sum)

#2. WAP to find the factorial of first n numbers. (using for)  
n =5
fact = 1
i=1
while i<=n:
    fact *= i
    i +=1
print ("factorial" ,fact )


n= 5
fact =  1
for i in range(1, n+1):
    
    fact *= i
print( "Factorial  :" , fact)

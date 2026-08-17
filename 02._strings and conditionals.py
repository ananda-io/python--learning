#ESCAPE SEQUENCE CHARACTERS : ~
str1 = "this is a string .\n we are creating in python" # \n is an character which prints NEXT LINE .
print(str1)
str2 = "to get a tab\t space we add this"
print (str2)
#. CONCATENATIONS 
# adding strings
str1 = 'anandaa'
str2 = "vattipalli"
final_str = str1+str2
print(final_str)
#lenght of string
str3 = "harshitha"
print(len(str3))
str4 = "harshitha"+" "+"vattipalli"
print(str4)
print(len(str4))

# INDEXING : ~
#index - position for every word in string. and the numbering starts from 0 ,1,2 etc...
# it hepls to access characters
str6 = "anu v"
print(str6[4])

#SLICING : ~ ( important for ml)
#accesing parts of a string
# str[starting_indx : ending_indx]#ending index is not included.

str = 'anamikaa'
print(str[2:7])# amika
str = "apna college"
print(str[0:5])
print(str[5:len(str)])
print(str[5:12])
print(str[5:len(str)])
print(str[5:])# last string
print(str[:12])#0
# SPECIAL CASE OF SLICING :
#negative index (we can count backward)
str = "apple"
print(str[-5:])

#STRING FUNCTIONS   
#1.ends with:--
str = "iam a coder"
print(str.endswith("er"))#return true if string ends with substr
#2.captalize:--
print(str.capitalize())# captalizes first charecter and rest of the letters to the lower case.
#3.replace:(old,new)replaces all occurencess of old(don't forget to use ,)
str= "iam studying python"
print(str.replace("o", "a"))
str = "she codes well"
print(str.replace("she codes well","she is a coder"))
#4.find:(word)returns 1st index of 1st occurrer.
str= "iam from college"
print(str.find("from"))#4 # for invalid cases it will print -1.
#5.count:("am") counts the occurence of substr
str = "apna college"
print(str.count("l"))
#                                              ~PRACTICE~
# 1 . WAP to input user's first name &print it's lenght.
name = input("what is your name : ")
print("lenght of your name is ", len(name))

#2.WAP to find the occurrence of $ in a string.
str= "this is the2nd problem"
print(str.count("$"))#0

#C0NDITIONAL SATATEMENTS : ~
#1. if
age = 20

if(age>=18):
    print("can apply for voter id")#proper spacing INDENTATION.
    print("can drive")

if(True):
   print ("can apply for the driving licence")
   # statements will exicute
#2.elif
light = "red"

if(light == "green"):
    print("go")
elif(light=="red"):
   print("stop")
elif(light == "yellow"):
   print("wait")

#3.else : 
age = 17
if(age>=18):
    print("can vote")
else:
    print ("cannot vote")

#grade students based on marks :
marks =int(input("enter students marks :"))
if(marks>=90):
    grade= "A"
elif(marks>=80 and marks <90):
    grade = "B"
elif(marks>=70 and marks < 80):
    grade= "C"
else:
    grade= "D"

print("grade of the student is ->", grade)

#NESTING :~
age = 95
if(age >= 18):
    if(age>=80):
        print( 'cannot drive')
    else:
        print("can drive")
else:
    print("cannot drive")  

                                                    #PRACTISE : ~
# WAP to check if a number entered by the user is odd or even.
number = int(input("enter the number please : "))
if(number%(2)==0):
    print ("it is an even number")
else:
    print (" it is an odd number")


#WAP to find the greatest of 3 numbers entered by the user.
a = int(input("please enter number 1 : "))
b = int(input("please enter number 2 : "))
c = int(input("please enter number 3 : "))
if(a >b and a>c):
    print("frist number is largest" , a)
elif(b>a and b>c):
    print("second number is the largest",b)
elif(c>b and c>a):
    print("third number is the largest", c)


#WAP to find the greatest of 4 numbers entered by user.
e = int(input("enter number 1: ")) 
f = int(input("enter number 2: "))
g = int(input("enter number 3: "))
h = int(input("enter number 4: "))
if(e>f and e>g and e>h):
    print("number 1" , e)
elif(f>e and f>g and f>h):
    print("number2 ", f)
elif(g>e and g>f and g>h):
    print ('third number', g)
elif(h>e and h>f and h>g):
    print("fourth number", h)


#WAP to check if a number is a multiple of 7 or not.
numb = int(input("enter number : "))
if(numb%7==0):
    print("it is multiple of 7")
else:
    print("it is not a multiple of 7")

    #                                                    end
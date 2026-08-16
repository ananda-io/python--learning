#variables and data  types
#first we learn to how to print a text 

print("hello world")
# VARIABLES : ~
"""a varible is a name given to a memory location in a program
example : """
name1 = "anu"
print(name1)

# IDENTIFIERS : ~
# it can be defined has name of the variable for an example here named the variable as name1 so this name1 is called as IDENTIFIER .
# And this identifier can be upper case or lower case,digits or an underscore.
# we can't add number in starting of identifier like (1 variable) it can accept like (variable 1).
# we can't use any special symbols like(!,@,#,%,& etc...)
# and it does't matter what the lenght of the identifier.


# DATA TYPE : ~ #
#Majourly those are 5 types 
"""1. float ,#decimal values
   2. integers ,# whole numbers (+,0,-)
   3. string # definetly in quatations wheter single , double or triple.
   4. bollean # True or False
   5. none # """
# if we want to print the type of the parameters...do this.
print(type("hello world")) # and the out put will be string
# example:
name = 'student'
age = '17'
weight = 50.1
print(type(name))#str #anything in quatation whether its number or integer
print(type(age))#int 
print(type(weight))#float
p = 5
q = 3
print(p>=q)# boolean #true
print(type(p>=q))
print(type(p<=q))
# none means nothing
w = None
print(None)# None
print(type(None))



# KEYWORDS : ~
              # are the reserved words in python.
              #python is a case sensitive language.
 

# TO PRINT SUM OR DIFFERENCE : ~
a = 2
b = 5
sum = a+b
diff = a-b
print(a+b)
print(a-b)

# TO PRINT COMMENTS : ~
# single line comment
"""
multi line
comment
""" 


# TYPE OF OPERATORS : ~
# an operation is asymbol that performs acertain operation between operands
# >arthematic operator : (+,-,*,/,%,**) add, sub ,mult, divid,to find remainder (modulo),power operator(**)a^b.

# >rational/comparision operators : (==, !=, >, <, >=, <=)
a=5
b=3
print(a==b)#false
print(a!=b)#true
#same for every operator

# >assignment operators (=, +=, -=, *=, /=, %=, **=)
num = 20
num = num + 10 # this can shortiy written ha num += 10.
numb1 = 20
numb1 -= 10
numb2 = 20
numb2 *= 10
numb3 = 10
numb3/= 10
numb4 = 12
numb4 %= 10
numb5 = 2
numb5 **= 2

print("num :", num)
print("num-=", numb1)
print("num*=", numb2)
print("num /=", numb3)
print("num:",numb4)
print("numb:",numb5)

#>logical operators (not,and,or)
# . not (returns opposite of bollean)
print(not False)
print(not True)
a = 3
b = 4
print(not(a>b))

#. and operator (it gives ture if both are true otherwise false)
val1 = True
val2 = True
print("AND operator:", val1 and val2)

#. or operator ( gives ture if 1 atleast one value is true
A = 4
B = 5
print("OR operator :",(a==b)or(a<b))


#TYPE CONVERSIONS : ~
#a,b = 1,2.0
#sum=a+b which has no errror
#but in a,b = 1, "2 "
# sum + a+b it gives an erroe because noe b is an string so for that"
#TYPE CASTING :
a,b = 1, "2"
c = int(b)
sum = a+c # no error
print(sum)


#INPUT IN PYTHON : ~
#Statement is used to accept values (using keyboard) from user.
int()
int(input())#int
float(input())#float

#                                                     ~PRACTICE QUESTIONS~



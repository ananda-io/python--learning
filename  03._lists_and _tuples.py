# LISTS :~
marks1 = 94.4
marks2 = 87.5
marks3 = 92.5
marks4 = 89.5

marks = [94.4, 87.5, 92.5, 89.5]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

student = ["karan",90,67.5,17,"telangana"]
print(student)

str = "hello"
print(str[0])
#str[0]="y" pythin will not accept this , because string objects does not support item aassignment.

student = ["karan",90,67.5,17,"telangana"]
print(student[0])
student[0] = "arjun"
print(student[0])
print(student)

#LIST SLICING :# same rules as that of string slicing.
marks = [90,92,94,96]
print(marks[0:3])
print(marks[-4:-1])

# LIST METHODS : (list specific)
#1. list.append()
x = [2,3,4]
x.append(8)
print(x)

 #2. list.sort()
y = [2,6,3,8,5]
y.append(9)
y.sort()
print(y)

z = [7,3,6]
z.sort(reverse=True)
print(z)

list = ["apple","carrot", "banana"]# string sorting is also possible (based on character)
list.sort()
print(list)

#3. list.reverse : #reverses the whole list
list = ['a','b','c','d']
list.reverse()
print(list)

#4. list.insert(idx,el) : #insert element at index :
list = [2,45,6]
list.insert(1,5)
print(list)

#5,6 ; list.remove() ,list.pop(idx) :
list=[1,2,3,4,5,6]
list.remove(4)
print(list)
list.pop(1)
print (list)



#  TUPLES IN PYTHON :~
tup = (2,3,7)
print(type (tup))
print(tup[0])
print(tup[1])
#tup[0] = 5 # tuple object does not support item assignment.

tup = ()
print(tup)
print(type(tup))

tup =(1,)# for single value tapule add a comma(,) if dont python takes it has integer.
print(tup)
print(type(tup))

# Slicing in tuples :
tup = (1,2,3,4)
print(tup[1:3])

# TUPLE METHOD : ~
#1.tup.index(el) returns index of first occurrence 
tup = (1,2,3,4,1)
print(tup.index(1))
print(tup.count(1))
 #                                                         ~PRACTICE~
 #1. WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
x = (input("enter name of movie 1 : "))
y = (input("enter name of movie 2 : "))
z = (input("enter name of movie 3 : "))
fav_movies = [x,y,z]
print("3 favorite movies name are ",fav_movies)
print(type(fav_movies))
  # or
movies = []
movies.append(input("enter 1st movie :"))
movies.append(input("enter 2nd movie :"))
movies.append(input("enter 3rd movie :"))
print(movies)

#2. WAP to check if a list contains a palindrome of elements.(hint : use copy()method)
 #       [1,2,3,2,1] [1,"abc","abc",1] 
 # palindrome -> maam (same feom font back)
list1 =[1,2,1]
list2 =[1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else: 
    print("NOT palindrome")

#3. WAP to count the number of dtudents with the "A" grade in the following tuple.
tup = ("C","D","A","A","B","B","A",)
print(tup.count("A"))

#4. store the above values in a list & sort them from "A" to "D".
grade = ["C","D","A","A","B","B","A",]
grade.sort()
print(grade)
#                                                         end
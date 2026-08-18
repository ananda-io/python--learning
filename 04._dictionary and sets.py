info = {
    "key" : "value",
    "learning" : "python",
    "age" : 17,
    "is adult" : False,
    "percentage" : 98.9
}
print(info)

details = {
    "name" : "ashitha",
    "subjects" : ["python","c","java"],# can also stored in diff data types (list)
    "topic" : ("dict","sets"), # tuple
}
print(details)
print(type(details))
# the (value) in dictionary can acceept diff datatypes(almost all)
# but in (key) we can't use lists and dictionaries, 
# key can be floating, string,numb,boolean, tuple also
# simple thing key should be immutable(un changable).
# dict are unordered.(no index)
#dict is mutable , don't allow duplicate keys

#to acess values of index instead of index we do
print(details["subjects"])
# we can change too
details["name"] = "V. vatsav" 
print(details)
# to add  new value
details["surname"]= 'v'
print(details)

null_dict ={}
print (null_dict)


#NESTED DICTIONARIEAS : ~
student = { 
    "name" : "sun",
    "subjects" : {
        "phy" : 97,
        "che" : 98,
    }
} # nested dictionaries.
print(student)
print(student["subjects"]["che"])
#  DICTIONARY METHODS :~

 #1 . myDict.keys() returns all keys
print(student.keys())
# also if we want type cast it in th e form of list example'
# float(8), in same way
print(list(student.keys()))
# to find total no. of keys in a dict, we can
print(len(student)) # total no.of key value pairs
print(len(list(student.keys())))

#2.myDict.values() # returns all values
print(student.values())
print(list(student.values()))

#3. myDict.items() # returns all (key,val) pairs as tuples
print(student.items())
print(list(student.items()))
pairs = (list(student.items()))
print (pairs[0])
print(pairs[1])

#4. myDict.get("key") # returns the key according to value
print(student["name"])
print(student.get("name"))
# we nedded 2 methods for thing
#print(student["name 2"]) ---> prints error
print(student.get("name 2")) # ---> prints None
# it helps to avoid errors

#5. myDict.update{new Dict} # inserts the specified items to the dictionary.
student.update({"city": "telangna"})
print ( student)


#SETS IN PYTHON : ~
collection = {1,2,3,4, "hello", "hello"} # duplicate values will be ignored.

print(collection)
print(type(collection))
print(len(collection))

# empty set : ~
empty = {} # but this is a dictionary
empty = set() # empty set; syntax

print(type(empty))

#methods in sets
collection = set()
#1.set.add(el)
collection.add(1)
collection .add(2)
collection.add("string")

#2.set.remove(el)
collection.remove(1)
# collection.add([1,2,3]) prints error because it doesn't accepts lists as they are mutable.
print(collection)
#3.set.clear() empties the set

#4.set.pop # removs random value
group = { "hello","apna college","world"}
print(group.pop())
print(group.pop())

#5.set.union(set2) # combines both set value and returns new
set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2))

#6. set.intersection(set2)
print(set1.intersection(set2))  

#                                               ~PRACTICE~
#1. store following word meanings in a python dictionary :
# take : "a piece of furniture","list of facts & figures" 
#cat : "a small animal"

meanings = {
    "take" : ["a piece of furniture","list of facts & figures"] ,
    "cat" : "a small animal"
}
print(meanings)


#2. you are given alist of subjects for students . Assume one classroom is required for 1 subject. 
# How many classrooms are needed by all students.

#"python","java","C++","python","javascript",
#"java,"python,"java","C++","C"

subjects = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(subjects))


#3. WAP to enter marks of 3 subjects from the user and store them in a dictionary . 
# .use subject name as key &marks as value.
subject1 = int(input("enter marks of subject1 : "))
subject2 = int(input("enter marks of subject2 : "))
subject3 = int(input("enter marks of subject3 : "))

marks = {"maths" : subject1,
         "physics" : subject2,
         "chemistry" : subject3
         }
print(marks)


#4. figure out a way to store 9 & 9.0 as separate values in the set.
#(you can take help of built-in data types)
set1 = {9 , "9.0"}
print(set1)

# or

set2 = {
   ("float",9.0),
   ("int",9)
}
print (set2)

 #                                                  ~END~
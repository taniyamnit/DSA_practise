from collections import namedtuple

#Declaring NamedTuple
Student = namedtuple('Student',["name","age","stream","dob"])

#Adding Values
S=Student('Taniya','30','Science','03031992')

#getting age using index
print("The Student's age using index is",S[1])

#getting age using keyname
print("The student's age using keyname is",S.age)

#adding another student
S1 = Student('Kiran','35','Commerce','10121988')
print("S1=",S1)

#access using getattr
print("the dob using getattr() is: ", getattr(S,"dob"), getattr(S1,"dob"))

Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x,p.y)

list = ['naman','20','Sci','15091999']
S2 = Student._make(list)
print(S2)

#printing the tuple as Ordered Dictionary
print(S1._asdict())

# initializing dict
di = {'name': "Nikhil", 'age': '19','stream': 'Commerce', 'dob': '1391997'}

#using “**” to convert the input list into namedtuple.
S3 = Student(**di)
print(S3)

# using _fields to display all the keynames of namedtuple()
print(Student._fields)

#._replace returns a new namedtuple , it does not modify the old one
print(S1._replace(name = "xyz"))
print(S1)

# Student.__new__ returns a new instance of Student(name,age,DOB)
print(Student.__new__(Student, 'Himani',"21","Sci","091012002"))

print(S1.__getnewargs__())
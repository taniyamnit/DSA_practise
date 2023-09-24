dict = {"Name":"Taniya","age":31,"subject":["physics","chemistry","maths"], "marks":[100,95,99]}
print("Creating Dictionary")
print(dict)

print("Accessing an element using key")
print("Name of the student is:", dict["Name"])

print("Accessing an element using get")
print(dict.get("age"))
print(dict.get("Name"))

print("Creation using Dictionary Comprehension")
myDict = {x:x**2 for x in [1,2,3,4,5]}
print(myDict)
myDict_1 = {x:x+2 for x in [1,2,3,4,5]}
print(myDict_1)

print("Creation of Dictionary using Zip")
keys = ["english","maths","physics", "chemistry", "cs"]
values = [90,92,80,79,95]
temp = {}
for key , value in zip(keys,values):
    temp[key]= value
print(temp)




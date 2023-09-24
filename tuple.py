#creating tuple with the use of Strings
t = ("dsa","java")
print("Creating Tuple with the use of Strings")
print(t)
print(type(t))

#creating tuple with the use of Integers
t1 = (1,2,3,4,5,-6,10)
print("creating tuple with the use of Integers")
print(t1)
print(type(t1))

#creating tuple using a list of integers
list1= [1,2,3,4,5,6,7,8,9,10]
t2 = tuple(list1)
print("Created Tuple using a list of numbers")
print(t2)

#accessing negative index of the tuple
print(t1[-2])
print(t2[-2])

#creating tuple using a 2dlist of integers
list = [[1,2],[3,4]]
print("Created Tuple using a 2d list of numbers")
t3 = tuple(list)
print(t3[0][1])

#creating tuple using a 2d list of integers
list = [[1,2],[3,4],[5,6]]
print("Created Tuple using a 2d list of numbers")
t4 = tuple(list)
print(t4[2][1])
print(type(t4))
print(type(list))

l =[1]
t = tuple(l)
print(t)
print(type(t))

from collections import Counter

print("We are using Counter in different ways")

print("With Sequence of Items")
print(Counter(['A','B','B','A','C','B','D','D','D','D','D']))

print("With dictionary")
count =Counter({'A':3,'B':2,'C':1})

print(count)

count.update(['A',1])
print(count)

# with keyword arguments
print(Counter(A=3, B=5, C=2))

# Count distinct elements and print Counter aobject
# Create a list
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
 

print(Counter(z))

#access all the keys and values of a counter
print(count.keys())
print(count.values())
print(count.items())

# Python program to demonstrate that counts in
# Counter can be 0 and negative

c1 = Counter(a=10,b=3,c=4)
c2 = Counter(a=4,b=3,c=10)
c1.subtract(c2)
print(c1)
print(c2)
c2.subtract(c1)
print(c1)
print(c2)

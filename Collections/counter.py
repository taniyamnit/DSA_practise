from collections import Counter

print("We are using Counter in different ways")

print("With Sequence of Items")
print(Counter(['A','B','B','A','C','B','D','D','D','D','D']))

print("With dictionary")
count =Counter({'A':3,'B':2,'C':1})

print(count)

count.update(['A',1])
print(count)



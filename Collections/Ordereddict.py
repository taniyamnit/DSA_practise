from collections import OrderedDict
#Orderedict is also a subclass of dictionary but unlike dictionary it remembers the order of the elements in which they were inserted
#normal dictionary
d = {}
d['a']=1
d['b']=2
d['c']=3
d['d']=4
#before deleting
print("before deleting")
for x , y in d.items():
    print(x,y)

d.pop('a')   

print("after deleting")
for x , y in d.items():
    print(x,y)

d['a']=1

print("after insertion")
for x , y in d.items():
    print(x,y)


#Ordered Dictionary

od = OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4

#before deleting
print("before deleting")
for x,y in od.items():
    print(x,y)

print("after deleting")
od.pop('a')

#after deleting
for x,y in od.items():
    print(x,y)


od['a']=1
print("After insertion")
for x,y in od.items():
    print(x,y)

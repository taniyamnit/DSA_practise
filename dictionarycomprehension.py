#creating Dictionary using Zip
keys = [1,2,3,4,5]
values = [6,7,8,9,10]
dict = { x:y for x,y in zip(keys,values)}
print(dict)

#creating dictionary using comprehension
dict2 = {x:x**2 for x in [1,2,3,4,5]}
print(dict2)

#creating dictionary fromkeys
dict3 = dict.fromkeys(range(5), True)
print(dict3)

#creating dictionary using zip and range
dict4 = {x:y for x , y in zip(range(5),range(10))}
print(dict4)

#creating dictionary using Comprehension
strdict = {x.upper():x*3 for x in 'coding'}
print(strdict)

#creating dictionary using if condition
dict5 = { x:x**3 for x in range(10) if x**3%4 ==0}
print(dict5)

#creating dictionary using nested comprehension
l = "tan"
dict6 ={x : { y: x+y for y in l} for x in l}
print(dict6)



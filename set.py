#create a set with mixed values types , numbers & strings
Set = set([1,2,"Computers", 4 , 0.5 , "Bangalore"])
print("\n Set with the use of Mixed Values")
print(Set)

#accessing elements using for loop
print("\n Elements of Set:")
for i in Set:
    print(i, end = " ")
print()

#checking the element using in keyword
print("Computers" in Set)

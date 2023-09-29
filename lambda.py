a = lambda x,y,z : x+y+z
print(a(10,20,30)) 

def my_func(n):
    return lambda a : a*n
    
mydoubler = my_func(2)
print(mydoubler(20))




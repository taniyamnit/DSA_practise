
def addition(e,f, *args):
    add = e+f
    for num in args:
        add+= num
    return add
print(addition(1,2,3,4,5))


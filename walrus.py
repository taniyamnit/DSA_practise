names = ["Taniya", "Jay","Suneeta"]
if(name:= input("Enter a name")) in names:
    print(f"Hello {name}")
else:
    print(f"{name} not found")
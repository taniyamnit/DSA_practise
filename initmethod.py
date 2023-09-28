class Person:
    #init method or constructor
    def __init__(self,name) -> None:
        self.name = name

    #Sample Method
    def say_hi(self):
        print("Hello my name is",self.name)
    
p = Person("Taniya")
p.say_hi()
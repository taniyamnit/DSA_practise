from collections import UserString
class Mystring(UserString):
    def append(self,s):
        self.data +=s
    
    def remove(self,s):
        self.data = self.data.replace(s,"")

s1 = Mystring(input())
s1.append("k")
s1.remove("a")

print(s1)

    
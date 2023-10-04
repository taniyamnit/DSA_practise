class Node:
    def __init__(self,data) -> None:
        self.data= data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data, end='->')
            temp=temp.next

if __name__ == '__main__':
    list1= LinkedList()
    list1.head = Node(1)
    second = Node(2)
    third = Node(3)
    list1.head.next = second
    second.next = third

list1.printlist()
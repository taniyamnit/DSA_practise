class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self) -> None:
        self.head = None
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = '->')
            temp = temp.next

if __name__ == '__main__':
    mylist = LinkedList()
    mylist.head= Node(1)
    second = Node(2)
    third = Node(3)
    mylist.head.next= second
    second.next= third

mylist.printList()

    



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Add a node to the end of the linked list
    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Search for a node with a specific data value
    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

    # Insert a node at a specified position
    def insert_at_position(self, data, position):
        if position < 0:
            return
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        prev = None
        count = 0
        while current and count < position:
            prev = current
            current = current.next
            count += 1
        if count == position:
            prev.next = new_node
            new_node.next = current

    # Delete a node with a specific data value
    def delete(self, target):
        if not self.head:
            return
        if self.head.data == target:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while current:
            if current.data == target:
                prev.next = current.next
                return
            prev = current
            current = current.next

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Merge two linked lists
    def merge(self, other_list):
        current = self.head
        while current.next:
            current = current.next
        current.next = other_list.head

    # Detect and remove loops (Floyd's cycle detection algorithm)
    def detect_and_remove_loop(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                self.remove_loop(slow)
                return True
        return False

    def remove_loop(self, loop_node):
        ptr1 = self.head
        while ptr1.next != loop_node:
            ptr1 = ptr1.next
        ptr2 = loop_node
        while ptr2.next != loop_node:
            ptr2 = ptr2.next
        ptr2.next = None

    # Find the middle node
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    # Check if the linked list is a palindrome
    def is_palindrome(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values == values[::-1]

    # Split the linked list into two halves
    def split_in_half(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next
        slow.next = None
        return self, LinkedList(second_half)

    # Remove duplicates from the linked list
    def remove_duplicates(self):
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    # Get Nth node from the end
    def get_nth_from_end(self, n):
        if n <= 0 or not self.head:
            return None
        slow = self.head
        fast = self.head
        for _ in range(n):
            if fast:
                fast = fast.next
            else:
                return None
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.data if slow else None

    # Display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    my_list = [1,2,3,4,5,6,7,8,9,10]
    for x in my_list:
        linked_list.add(x)
    
    linked_list.display()  # Output: 1 -> 2 -> 3 -> None
    
    print("Search for 2:", linked_list.search(2))  # Output: Search for 2: True
    
    linked_list.insert_at_position(4, 1)
    
    linked_list.display()  # Output: 1 -> 4 -> 2 -> 3 -> None
    
    linked_list.delete(2)
    
    linked_list.display()  # Output: 1 -> 4 -> 3 -> None
    
    linked_list.reverse()
    
    linked_list.display()  # Output: 3 -> 4 -> 1 -> None

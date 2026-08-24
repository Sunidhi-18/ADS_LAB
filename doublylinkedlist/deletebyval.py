class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to next node
        self.prev = None  # Pointer to previous node

class DoublyDeleteList:
    def __init__(self):
        # Create a pre-filled list: 10 <-> 20 <-> 30
        self.head = Node(10)
        second = Node(20)
        self.head.next = second
        second.prev = self.head
        
        third = Node(30)
        second.next = third
        third.prev = second

    def delete(self, key):
        current = self.head                 # Start looking from the head
        
        # Case 1: The node to delete is the head node
        if current is not None and current.data == key:
            self.head = current.next        # Move head to the next node
            if self.head is not None:
                self.head.prev = None       # Clear the new head's previous pointer
            print(f"Deleted {key} from the list.")
            return

        # Case 2: Search for the node in the middle or end
        while current is not None and current.data != key:
            current = current.next          # Move forward until we find the key

        # If key was not found in the list
        if current is None:
            print(f"Value {key} not found.")
            return

        # Bypass 'current' by updating its neighbors' pointers
        if current.next is not None:
            current.next.prev = current.prev # Point next node's prev back to previous node
            
        if current.prev is not None:
            current.prev.next = current.next # Point prev node's next forward to next node
            
        print(f"Deleted {key} from the list.")

    def print_list(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print("List: None <-> " + " <-> ".join(elements) + " <-> None")

my_list = DoublyDeleteList()
print("Before deletion:")
my_list.print_list()

my_list.delete(20)

print("After deletion:")
my_list.print_list()
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to next node
        self.prev = None  # Pointer to previous node

class DoublySearchList:
    def __init__(self):
        # Create a pre-filled list: 10 <-> 20 <-> 30
        self.head = Node(10)
        second = Node(20)
        self.head.next = second
        second.prev = self.head
        
        third = Node(30)
        second.next = third
        third.prev = second

    def search(self, key):
        current = self.head                 # Start searching from the head node
        position = 0                        # Keep track of position index
        while current is not None:          # Loop through nodes until the end
            if current.data == key:         # Check if current node matches target value
                print(f"Found {key} at position {position}!")
                return True                 # Exit since we found it
            current = current.next          # Move forward to the next node
            position += 1                   # Increase position count
        print(f"Value {key} not found.")    # Print if search fails
        return False

my_list = DoublySearchList()
my_list.search(20)
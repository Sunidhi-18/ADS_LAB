class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyDeleteTailList:
    def __init__(self):
        # Pre-populate list: 10 <-> 20 <-> 30
        self.head = Node(10)
        second = Node(20)
        third = Node(30)
        
        self.head.next = second
        second.prev = self.head
        second.next = third
        third.prev = second

    def delete_at_end(self):
        if self.head is None:                  # Check if list is empty
            print("The list is empty.")
            return

        # Case 1: If there is only one node in the list
        if self.head.next is None:
            print(f"Deleted tail node with value: {self.head.data}")
            self.head = None
            return

        # Case 2: Traverse until we find the last node
        current = self.head
        while current.next is not None:
            current = current.next             # Move forward until 'current' is the last node

        deleted_data = current.data            # Save the last node's data
        current.prev.next = None               # Cut the link from the second-to-last node
        print(f"Deleted tail node with value: {deleted_data}")

    def print_list(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print("List: None <-> " + " <-> ".join(elements) + " <-> None")

# --- Run the code ---
my_list = DoublyDeleteTailList()
print("Before deletion:")
my_list.print_list()

my_list.delete_at_end()  # Removes 30

print("After deletion:")
my_list.print_list()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyDeleteHeadList:
    def __init__(self):
        # Pre-populate list: 10 <-> 20 <-> 30
        self.head = Node(10)
        second = Node(20)
        third = Node(30)
        
        self.head.next = second
        second.prev = self.head
        second.next = third
        third.prev = second

    def delete_at_beginning(self):
        if self.head is None:                    # Check if list is empty
            print("The list is empty.")
            return

        deleted_data = self.head.data            # Save data of current head
        
        if self.head.next is not None:           # If there is more than one node
            self.head = self.head.next           # Move head pointer to the second node
            self.head.prev = None                # Clear the new head's 'prev' pointer
        else:
            self.head = None                     # If it was the only node, make list empty
            
        print(f"Deleted head node with value: {deleted_data}")

    def print_list(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print("List: None <-> " + " <-> ".join(elements) + " <-> None")

# --- Run the code ---
my_list = DoublyDeleteHeadList()
print("Before deletion:")
my_list.print_list()

my_list.delete_at_beginning()  # Removes 10

print("After deletion:")
my_list.print_list()
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to next node
        self.prev = None  # Pointer to previous node

class DoublyInsertHeadList:
    def __init__(self):
        self.head = None  # Start with an empty list

    def insert_at_beginning(self, data):
        new_node = Node(data)                  # Step 1: Create the new node
        if self.head is not None:              # Check if the list already has nodes
            new_node.next = self.head          # Step 2: Point new node's next to the current head
            self.head.prev = new_node          # Step 3: Point current head's prev back to new node
        self.head = new_node                   # Step 4: Make the new node the head of the list
        print(f"Inserted {data} at the beginning.")

    def print_list(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print("List: None <-> " + " <-> ".join(elements) + " <-> None")

# --- Run the code ---
my_list = DoublyInsertHeadList()
my_list.insert_at_beginning(20)  # List: 20
my_list.insert_at_beginning(10)  # List: 10 <-> 20
my_list.print_list()
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node

class InsertAtHeadList:
    def __init__(self):
        self.head = None  # Start with an empty list

    def insert_at_beginning(self, data):
        new_node = Node(data)          # Step 1: Create a new node with the data
        new_node.next = self.head      # Step 2: Point new node's next to the current head
        self.head = new_node           # Step 3: Make the new node the new head
        print(f"Inserted {data} at the beginning.")

    def print_list(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print("List: " + " -> ".join(elements) + " -> None")

# --- Run the code ---
my_list = InsertAtHeadList()
my_list.insert_at_beginning(20)  # List becomes: 20
my_list.insert_at_beginning(10)  # List becomes: 10 -> 20
my_list.print_list()
class Node:
    def __init__(self, data):
        self.data = data
        self.next =None

class delfront:
    def __init__(self):
        self.head = Node(10)
        self.head.next = Node(20)
        self.head.next.next = Node(30)

    def del_at_front(self):
        if self.head == None:
            print("the list is already empty.")
            return

        deleted_data = self.head.data
        self.head = self.head.next
        print("deleted head node with value: ", deleted_data)

    def print_list(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print("list: " + " -> ".join(elements) + " -> None")

my_list =delfront()
print("before deletion:")
my_list.print_list()

my_list.del_at_front()

print("after deletion:")
my_list.print_list()

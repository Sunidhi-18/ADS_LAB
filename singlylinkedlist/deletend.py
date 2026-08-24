class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class delend:
    def __init__(self):
        self.head = Node(10)
        self.head.next = Node(20)
        self.head.next.next = Node(30)

    def del_at_end(self):
        if self.head is None:
            print("nothing to delete.")
            return

        if self.head.next is None:
            print("deleted last node with value:", self.head.data)
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next

        deleted_data = current.next.data
        current.next = None
        print("deleted tail node with value: ", deleted_data)

    def print_list(self):
        current = self.head
        elements =[]
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print("list: " + " -> ".join(elements) + "->None")

my_list = delend()

print("before deletion:")
my_list.print_list()

my_list.del_at_end()

print("after deletion:")
my_list.print_list()

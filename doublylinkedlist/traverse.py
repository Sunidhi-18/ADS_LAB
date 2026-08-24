class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubletraverse:
    def __init__(self):
        self.head = Node(10)

        second = Node(20)
        self.head.next = second
        second.prev = self.head

        third = Node(30)
        self.next = third
        third.prev = second

    def traverse(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next

my_list = doubletraverse()
my_list.traverse()
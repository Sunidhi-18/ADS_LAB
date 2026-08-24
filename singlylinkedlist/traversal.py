class Node:
    def __init__(self, data):
        self.data = data
        self.next =None

class traverseonlylist:
    def __init__(self):
        self.head = Node(10)
        self.head.next = Node(20)
        self.head.next.next = Node(30)

    def traverse(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print("list: "+"->".join(elements)+"->None")

my_list = traverseonlylist()
my_list.traverse()
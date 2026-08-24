class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class searchonlylist:
    def __init__(self):
        self.head = Node(10)
        self.head.next = Node(20)
        self.head.next.next = Node(30)

    def search(self, key):
        current = self.head
        position = 0
        while current is not None:
            if current.data == key:
                print(f"found {key} at position {position}!")
                return True
            current = current.next
            position +=1
        print(f"value {key} not found.")
        return False

my_list = searchonlylist()
my_list.search(20)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class deleteonlylist:
    def __init__(self):
        self.head = Node(10)
        self.head.next = Node(20)
        self.head.next.next = Node(30)

    def delete(self, key):
        current = self.head

        if current is not None and current.data == key:
            self.head = current.next
            print(f"deleted {key} from the list")
            return

        prev = None
        while current is not None and current.data!=key:
            prev = current
            current = current.next

        if current is None:
            print(f"value {key} not found")
            return

        prev.next = current.next
        print(f"deleted {key} from the list")

my_list = deleteonlylist()
my_list.delete(20)
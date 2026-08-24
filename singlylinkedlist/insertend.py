class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class InsertOnlyList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        print("successfully inserted: ", data)
    
my_list = InsertOnlyList()
my_list.insert(10)
my_list.insert(20)

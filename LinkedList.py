from Node import Node
class LinkedList():
    """docstring for LinkedList."""
    def __init__(self, head = None):
        self.head = head
    def get_head(self):
        return self.head
        
    def insert(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
    
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, key):
        current = self.head
        found = False
        while current and not found:
            if current.get_item() == key:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError ("Data Not In List")
        return current
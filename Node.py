from Item import Item
class Node():
    def __init__(self, item = None, next_node = None):
        self.item = item
        self.next_node = next_node
    
    def get_item(self):
        return self.item
    
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


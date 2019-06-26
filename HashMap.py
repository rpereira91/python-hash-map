from LinkedList import LinkedList
from Item import Item

class HashMap():

    def __init__(self, size):
        self.size = size
        self.hashmap = [[LinkedList()] for i in range(size**2)]

    def insert_item(self, item):
        hash_key = hash(item.get_key()) % len(self.hashmap)
        key_exists = False

        bucket = self.hashmap[hash_key]
        bucket.insert(item)

    def get_load_factor(self):
        return self.size * 0.75

hm = HashMap(10)
hm.insert_item(Item("001","test"))

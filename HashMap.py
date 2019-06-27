from LinkedList import LinkedList
from Item import Item

class HashMap():

    def __init__(self, size):
        self.size = size
        self.hashmap = [LinkedList() for i in range(size)]

    def insert_item(self, item):
        hash_key = hash(item.get_key()) % self.size
        bucket = self.hashmap[hash_key]
        if self.get_load_factor() <= 0.75:
            bucket.insert(item)
        else:
            self.re_create_hash()

    def get_load_factor(self):
        hash_size = 0
        for i in self.hashmap:
            hash_size += i.size()
        return hash_size / (self.size)
    
    def re_create_hash(self):
        old_hashmap = self.hashmap[:]
        self.size = self.size * 2
        self.hashmap = [LinkedList() for i in range(self.size)]
        for bucket in old_hashmap:
            if bucket.size():
                current = bucket.get_head()
                while current:
                    self.insert_item(current.get_item())
                    current = current.get_next()

hm = HashMap(10)
hm.insert_item(Item("001","test"))
print(hm.get_load_factor())
hm.re_create_hash()
print(hm.get_load_factor())

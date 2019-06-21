class HashMap(object):
    """docstring for HashMap."""
    def __init__(self):
        self.hashmap = [[] for i in range(256)]
    
    def insert_item(self, item):
        hash_key = hash(item.get_key()) % len(self.hashmap)
        key_exists = False
        bucket = self.hashmap[hash_key]
        for index, obj in enumerate(bucket):
            key = obj.get_key()
            if item.get_key() == key:
                key_exists = True
                break
        if key_exists:
            bucket[index] = (item)
        else:
            bucket.append(item)

    def get_item_value(self, key):
        hash_key = hash(key) % len(self.hashmap)
        bucket = self.hashmap[hash_key]
        for i, obj in enumerate(bucket):
            return obj.get_value()

class Item(object):
    """docstring for Item."""
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def get_value(self):
        return self.value
    def get_key(self):
        return self.key
    
hm = HashMap()
hm.insert_item(Item("001", "Item test"))
hm.insert_item(Item("010", "01 test"))

print(hm.get_item_value("001"))
print(hm.get_item_value("010"))
#dummy item class so I can practice inserting objects into the hashmap
class Item(object):
    """docstring for Item."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
    #basic getter and setter methods 
    def get_value(self):
        return self.value
    def get_key(self):
        return self.key
    def set_value(self, value):
        self.value = value
    def __str__(self):
        return str("Key : {} \tValue: {}".format(self.key, self.value))

    def __eq__(self, key):
        return key == self.key
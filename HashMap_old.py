#Notes:
# Get rid of iterating through the buckets, use indexOf to find element 
# Re-build the hashmap if there are a large number of elements 
# Get rid of the print statement in the Item Class
# Create my own linked list for the buckets
# Build a tree to find elements quicker 
from Item import Item
class HashMap(object):
    """docstring for HashMap."""
    def __init__(self):
        # create an array of buckets, normally buckets will be n^2
        self.hashmap = [[] for i in range(256)]
    #function to insert objects 
    def insert_item(self, item):
        #create the hash key using the built in hash function and moduloing it by the length of the hashmap
        # this ensures that it is within the range of the array size 
        hash_key = hash(item.get_key()) % len(self.hashmap)
        #boolean to make sure that key is unique
        key_exists = False
        #get the bucket that is in the index of the hash key
        bucket = self.hashmap[hash_key]
        #enumerate through the bucket looking for the key
        for index, obj in enumerate(bucket):
            #get they key of the object
            key = obj.get_key()
            #if the key exists we know to update the object
            if item.get_key() == key:
                key_exists = True
                break
        #update the object
        if key_exists:
            bucket[index].set_value(item.get_value())
        #add the object to the bucket list
        else:
            bucket.append(item)
    #gets the item from the key
    def get_item_value(self, key):
        #get the hash key using the same method as when it was set
        hash_key = hash(key) % len(self.hashmap)
        #set the bucket that is in the index of the hash key
        bucket = self.hashmap[hash_key]
        #go through the bucket and if they key matches one of the keys in the bucket return that object
        for obj in bucket:
            if obj.get_key() == key:
                return obj

    def get_map_size(self):
        return len(self.hashmap)

if __name__ == "__main__":
    # hm = HashMap()
    # hm.insert_item(Item("001", "Some random value"))
    # hm.insert_item(Item("010", "Another value or whatever"))

    # print(hm.get_item_value("001"))
    # print(hm.get_map_size())

    tes_item = Item("001", "Some random value")
    print(tes_item == "001")
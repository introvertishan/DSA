# Hash/Dictonary always have O(1) complexity.
# hash function hashes the object and maps it to a index.

# hash converts every letter to it ASCII value, sums it and then MODS it.
# Eg. ord('a') this returns 97

# look up by key is O(1)
# also insertion deletion always has complexity of O(1)

# key stores the value using hash function and stores at an index.


# when we try to insert a new object inside the hash map but the hash function returns a value of index which already
# has data, this is called collision.

# collision detection

# 1: Linear Chaining :  Storing multiple values at an index, using linked list. It only stores value.
# In best case scenario, it can have complexity of O(1) and in worst case it can be O(n)

# 2: Linear Probing : Here we stores both the key and value at an index in a tuple, but before storing multiple values
# at an index, it loops and looks for any free index.

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del", index)
                del self.arr[arr_index][index]
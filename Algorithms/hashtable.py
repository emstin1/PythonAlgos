class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [0 for x in range(size)]
        self.indexes = []
        self.keys = []
        self.values = []

    def collision(self, idx):
        return idx in self.indexes

    def hash(self, key):
        """this is a very naive hash implementation.  not suitable for anything"""
        int_string = sum([ord(x) for x in str(key)])
        return (int_string << 32)

    def key_to_index(self, key):
        return self.hash(key) % self.size

    def get(self, key):
        if key in self.keys:
            return self.table[self.key_to_index(key)]
        else:
            raise KeyError("key '{}' not found".format(key))

    def set(self, key, value):
        if key in self.keys:
            self.table[self.key_to_index(key)] = value
        else:
            idx = self.key_to_index(key)
            while True:
                if not self.collision(idx):
                    try:
                        self.table[idx] = value
                        self.keys.append(key)
                        self.values.append(value)
                        self.indexes.append(idx)
                        break
                    except IndexError:
                        raise IndexError("Table out of Room")
                else:
                    idx += 1

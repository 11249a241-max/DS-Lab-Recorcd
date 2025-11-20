class HashTable:
    def __init__(self, size=10):
        self.size = size; self.table = [[] for _ in range(size)]
    def _hash(self, key):
        return hash(key) % self.size
    def put(self, key, value):
        h = self._hash(key)
        for i, (k, v) in enumerate(self.table[h]):
            if k == key:
                self.table[h][i] = (key, value); return
        self.table[h].append((key, value))
    def get(self, key):
        h = self._hash(key)
        for k, v in self.table[h]:
            if k == key: return v
        return None
    def delete(self, key):
        h = self._hash(key)
        for i, (k, _) in enumerate(self.table[h]):
            if k == key:
                self.table[h].pop(i); return True
        return False

if __name__ == "__main__":
    ht = HashTable(5)
    ht.put("a", 1); ht.put("b", 2)
    print(ht.get("a")); ht.delete("a"); print(ht.get("a"))

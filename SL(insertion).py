class Node:
    def __init__(self, v):
        self.v = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, v):
        n = Node(v)
        n.next = self.head
        self.head = n

    def insert_tail(self, v):
        n = Node(v)
        if not self.head:
            self.head = n
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = n

    def insert_pos(self, v, pos):
        if pos == 0:
            self.insert_head(v)
            return
        n = Node(v)
        t = self.head
        for _ in range(pos - 1):
            if not t:
                return
            t = t.next
        if not t:
            return
        n.next = t.next
        t.next = n

    def display(self):
        r = []
        t = self.head
        while t:
            r.append(t.v)
            t = t.next
        return r

if __name__ == "__main__":
    l = LinkedList()
    l.insert_head(3)
    l.insert_tail(5)
    l.insert_pos(4, 1)
    print(l.display())

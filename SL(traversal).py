class Node:
    def __init__(self, v):
        self.v = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, v):
        n = Node(v)
        if not self.head:
            self.head = n
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = n

    def traverse(self):
        r = []
        t = self.head
        while t:
            r.append(t.v)
            t = t.next
        return r

if __name__ == "__main__":
    l = LinkedList()
    l.insert_tail(10)
    l.insert_tail(20)
    l.insert_tail(30)
    print(l.traverse())

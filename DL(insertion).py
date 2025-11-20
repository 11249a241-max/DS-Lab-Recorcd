class DNode:
    def __init__(self, v):
        self.v = v
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, v):
        n = DNode(v)
        n.next = self.head
        if self.head:
            self.head.prev = n
        self.head = n

    def insert_tail(self, v):
        n = DNode(v)
        if not self.head:
            self.head = n
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = n
        n.prev = t

    def display(self):
        t = self.head
        while t:
            print(t.v, end=" ")
            t = t.next

if __name__ == "__main__":
    d = DoublyLinkedList()
    d.insert_head(3)
    d.insert_tail(5)
    d.insert_head(2)
    d.display()

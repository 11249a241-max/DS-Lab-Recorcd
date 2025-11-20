class DNode:
    def __init__(self, v):
        self.v = v
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

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

    def delete_value(self, v):
        t = self.head
        while t and t.v != v:
            t = t.next
        if not t:
            return
        if t.prev:
            t.prev.next = t.next
        else:
            self.head = t.next
        if t.next:
            t.next.prev = t.prev

    def display(self):
        t = self.head
        while t:
            print(t.v, end=" ")
            t = t.next

if __name__ == "__main__":
    d = DoublyLinkedList()
    d.insert_tail(1)
    d.insert_tail(2)
    d.insert_tail(3)
    d.delete_value(2)
    d.display()

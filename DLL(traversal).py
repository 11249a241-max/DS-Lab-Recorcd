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

    def traverse_forward(self):
        t = self.head
        while t:
            print(t.v, end=" ")
            t = t.next

    def traverse_backward(self):
        t = self.head
        if not t:
            return
        while t.next:
            t = t.next
        while t:
            print(t.v, end=" ")
            t = t.prev

if __name__ == "__main__":
    d = DoublyLinkedList()
    d.insert_tail(10)
    d.insert_tail(20)
    d.insert_tail(30)
    d.traverse_forward()
    print()
    d.traverse_backward()

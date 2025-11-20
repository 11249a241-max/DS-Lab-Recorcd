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

    def display(self):
        t = self.head
        while t:
            print(t.v, end=" ")
            t = t.next

if __name__ == "__main__":
    l = LinkedList()
    l.insert_tail(5)
    l.insert_tail(10)
    l.insert_tail(15)
    l.display()

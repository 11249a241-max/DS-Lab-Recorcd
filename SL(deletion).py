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

    def delete_value(self, v):
        t = self.head
        prev = None
        while t and t.v != v:
            prev = t
            t = t.next
        if not t:
            return
        if prev:
            prev.next = t.next
        else:
            self.head = t.next

    def display(self):
        r = []
        t = self.head
        while t:
            r.append(t.v)
            t = t.next
        return r

if __name__ == "__main__":
    l = LinkedList()
    l.insert_tail(1)
    l.insert_tail(2)
    l.insert_tail(3)
    l.delete_value(2)
    print(l.display())

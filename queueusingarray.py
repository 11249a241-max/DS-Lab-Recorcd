class Queue:
    def __init__(self):
        self.a = []
        self.head = 0
    def enqueue(self, x):
        self.a.append(x)
    def dequeue(self):
        if self.head >= len(self.a):
            return None
        v = self.a[self.head]
        self.head += 1
        if self.head > 50 and self.head*2 > len(self.a):
            self.a = self.a[self.head:]; self.head = 0
        return v
    def is_empty(self):
        return self.head >= len(self.a)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10); q.enqueue(20)
    print(q.dequeue()); print(q.dequeue()); print(q.dequeue())

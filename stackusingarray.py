class Stack:
    def __init__(self):
        self.a = []
    def push(self, x):
        self.a.append(x)
    def pop(self):
        return self.a.pop() if self.a else None
    def peek(self):
        return self.a[-1] if self.a else None
    def is_empty(self):
        return not self.a

if __name__ == "__main__":
    s = Stack()
    s.push(1); s.push(2); s.push(3)
    print(s.pop()); print(s.peek()); print(s.is_empty())

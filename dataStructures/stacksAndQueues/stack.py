class Stack:

    def __init__(self):
        """
        initialize stack. LIFO
        """
        self.data = []

    def push(self, x: int) -> None:
        if not self.data:
            self.data = [x]
        else:
            self.data.append(x)

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1]


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(8)
    print(s.top())
    s.pop()
    print(s.top())
    s.push(9)
    print(s.top())
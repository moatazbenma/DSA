class MyStack:

    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, x: int) -> None:
        self.stackA.append(x)

    def pop(self) -> int:
        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop(0))
        return self.stackB.pop(-1)

    def top(self) -> int:
        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop(0))
        return self.stackB[-1]

    def empty(self) -> bool:
        return len(self.stackA) == 0 and len(self.stackB) == 0


obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)

print(obj.pop())
print(obj.top())
print(obj.empty())
class MyQueue:
    
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, x:int):
        self.stackA.append(x)

    def pop(self):
        self.stackA.pop()
        
        

    def peek(self):
        print(self.stackA[0])
    
    def empty(self):
        if len(self.stackA) == 0:
            print(True)
        else:
            print(False)
        
    def s(self):
        return self.stackA

    
    


queue = MyQueue()
queue.push(1)
queue.push(2)
queue.push(3)

queue.pop()

while queue.stackA:
    value = queue.stackA.pop()
    queue.stackB.append(value)


print(queue.stackB)


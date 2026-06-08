class MyQueue:
    
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, x:int):
        self.stackA.append(x)

    def pop(self):
        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop())

        return self.stackB.pop()
        
        

    def peek(self):
        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop())

        return self.stackB[-1]
    
    def empty(self):
        return len(self.stackA) == 0 and len(self.stackB) == 0
        


    
    


queue = MyQueue()
queue.push(1)



print(queue.stackB)


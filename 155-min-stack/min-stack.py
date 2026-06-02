class MinStack:

    def __init__(self):
        self.stack = []
        self.min_i = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_i or val <= self.stack[self.min_i[-1]] :
            self.min_i.append(len(self.stack) - 1)
    
             

        

    def pop(self) -> None:
        if self.stack[self.min_i[-1]] == self.stack[-1]:
            self.min_i.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack[self.min_i[-1]]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
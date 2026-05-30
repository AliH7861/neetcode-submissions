class MinStack:

    def __init__(self):
        self.items = []
        self.minVal = []

    def push(self, val: int) -> None:

        self.items.append(val)

        if(len(self.minVal) == 0 or val <= self.minVal[-1]):
            self.minVal.append(val)

    def pop(self) -> None:

        if(self.minVal[-1] == self.items[-1]):
            self.minVal.pop() 

        if(len(self.items) > 0):
            return self.items.pop()
        return None

    def top(self) -> int:
        if(len(self.items) > 0):
            return self.items[-1]
        return None

    def getMin(self) -> int:
       return self.minVal[-1]
        

class MinStack:

    def __init__(self):
        self.stk = []
        self.minstk = []
    
    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.minstk) < 1:
            self.minstk.append(val)
        else:
            self.minstk.append(min(val, self.minstk[-1]))

    def pop(self) -> None:
        self.stk.pop()
        self.minstk.pop()
        

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]
        

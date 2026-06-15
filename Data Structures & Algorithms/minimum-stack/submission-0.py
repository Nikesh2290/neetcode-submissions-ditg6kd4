class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mini)>0:
            x = self.mini[-1]
            mini = min(val,x)
            self.mini.append(mini)
        else:
            self.mini.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
        

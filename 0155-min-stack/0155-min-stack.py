class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []          # Stores the minimum value at each level

        # self.minNum = float('inf')  # Start with the largest possible value

    def push(self, value: int) -> None:
        self.stack.append(value)

        # Compare with the previous minimum and keep the smaller value
        value = min(value, self.minStack[-1] if self.minStack else value)
        self.minStack.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

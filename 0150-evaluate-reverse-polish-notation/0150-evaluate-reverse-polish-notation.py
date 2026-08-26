# Use int(a / b) because LeetCode wants division to truncate toward 0.
# Python's // rounds down, which gives the wrong result for negative numbers.
# Example: -7 // 2 = -4, but int(-7 / 2) = -3


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
                
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+": stack.append(a + b)
                elif token == "-": stack.append(a - b)
                elif token == "*": stack.append(a * b)
                else: stack.append(int(a / b))

        return stack[-1]
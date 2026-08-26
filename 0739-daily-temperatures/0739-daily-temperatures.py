#Brute Force O(n2)
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        n = len(temperatures)

        for i in range(n):
            found = False

            for j in range(i + 1, n):
                if temperatures[i] < temperatures[j]:
                    answer.append(j - i)
                    found = True
                    break

            if not found:
                answer.append(0)

        return answer
'''        



# Monotonic Stack - O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        # Stores [temperature, index] for unresolved days.
        # Temperatures in the stack stay monotonically decreasing.
        stack = []

        for index, temp in enumerate(temperatures):

            # Current temperature resolves previous colder days.
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()

                # Number of days between the two temperatures.
                res[stackIndex] = index - stackIndex

            # Current day is now waiting for a warmer future day.
            stack.append([temp, index])
        
        return res
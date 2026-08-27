class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        
        pairs = [[p,s] for p, s in zip(position, speed)]

        # Process cars from closest to target to farthest 
        for position, speed in sorted(pairs)[::-1]:

            # Time this car would take to reach the target
            time = (target - position) / speed
            stack.append(time)

            # If the current car takes less time to reach the target than
            # the fleet ahead, it is faster and will eventually catch that fleet.
            # Since cars cannot pass each other, they merge and become one fleet.
            # We remove the current car's time because it no longer forms
            # a separate fleet; the slower fleet's time is kept.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)
            
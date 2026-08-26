class Solution: 
    def isValid(self, s: str) -> bool: 
        # Store opening brackets
        stack = [] 

        # Match closing brackets with opening brackets
        closeToOpen = { 
            ")": "(",  
            "}": "{",  
            "]": "[" 
        } 
 
        for c in s: 
            if c in closeToOpen: 
                # Check if closing bracket matches the top
                if stack and stack[-1] == closeToOpen[c]: 
                    stack.pop() 
                else: 
                    # Brackets don't match
                    return False 
            else: 
                # It's an opening bracket, so add it to the stack
                stack.append(c) 
        
        # Valid if no opening brackets remain
        return not stack
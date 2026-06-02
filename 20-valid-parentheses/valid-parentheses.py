class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for ch in s :
            if ch == '(' or ch == '{' or ch == '[' :
                stack.append(ch)
            elif len(stack) == 0 :
                return False
            elif ch == ')'  :
                if stack.pop() == '(' :
                    continue
                else :
                    return False
            elif ch == '}' :
                if stack.pop() == '{' :
                    continue
                else :
                    return False
            elif ch == ']' :
                if stack.pop() == '[' :
                    continue
                else :
                    return False
        if stack == [] :
            return True
        return False


        
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(':')', '{':'}', '[':']'}
        if len(s) <= 1 :
            return False
        for i in s:
            if i in d:
                stack.append(i)
            if i in d.values():
                if len(stack) == 0:
                    return False
                if d[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True 
        else:
            return False
        
        
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        s = set(('+', '-', '*', '/'))
        for i in tokens:
            if i not in s:
                stack.append(int(i))
            else:
                temp = 0
                if i == '+':
                    temp = stack[-2] + stack[-1]
                if i == '-':
                    temp = stack[-2] - stack[-1]
                if i == '*':
                    temp = stack[-2] * stack[-1]
                if i == '/':
                    temp = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(temp)
        return stack[0]
        
class Solution:
    def isValid(self, s: str) -> bool:
        h={']':'[',')':'(','}':'{'}
        stack=[]
        for i in s:
            if i in ['[','(','{']:
                stack.append(i)
            else:
                if not stack or stack[-1]!=h[i]:
                    return False
                stack.pop()
        return len(stack)==0

        
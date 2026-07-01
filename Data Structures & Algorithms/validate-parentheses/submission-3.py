class Solution:
    def isValid(self, s: str) -> bool:
        x=[]
        h={']':'[','}':'{',')':'('}
        if len(s)<2:
            return False
        for i in s:
            if i in ['[','{','(']:
                x.append(i)
            else:
                if not x or x[-1]!=h[i]:
                    return False
                x.pop()
        return len(x)==0
        
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        n=len(s)
        x=[0]*26
        for ch in s:
            i=ord(ch)-ord('a')
            x[i]+=1
        for ch in t:
            i=ord(ch)-ord('a')
            x[i]-=1
        for i in x:
            if i!=0:
                return False
        return True

        
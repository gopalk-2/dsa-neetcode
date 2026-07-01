class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        x=[]
        for i in s:
            if 0<=ord(i.lower())-ord('a')<26 or 0<=ord(i.lower())-ord('0')<=9 :
                x.append(i.lower())
        n=len(x)
        i=0
        j=n-1
        while i<j:
            if x[i]!=x[j]:
                return False
            i+=1
            j-=1
        return True
        
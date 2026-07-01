class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resLengh=0
        n=len(s)
        for i in range(n):
            l=r=i
            while l>=0 and r<n and s[l]==s[r]:
                if len(s[l:r+1])>resLengh:
                   res=s[l:r+1]
                   resLengh=len(s[l:r+1]) 
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<n and s[l]==s[r]:
                if len(s[l:r+1])>resLengh:
                   res=s[l:r+1]
                   resLengh=len(s[l:r+1])
                l-=1
                r+=1
        return res
        
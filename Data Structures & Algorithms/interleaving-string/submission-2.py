class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo={}
        if len(s1)+len(s2)!=len(s3):
            return False
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i==len(s1) and j==len(s2):
                return True
            k=i+j
            ans=False
            if i<len(s1) and s1[i]==s3[k]:
                ans=dfs(i+1,j)
            if not ans and j<len(s2) and s2[j]==s3[k]:
                ans=dfs(i,j+1)
            memo[(i,j)]=ans
            return ans
        return dfs(0,0)      
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo={}
        def helper(s,wordDict):
            if s in memo:
                return memo[s]
            if s=="":
                return 1
            for word in wordDict:
                if s.startswith(word):
                    suff=s[len(word):]
                    if helper(suff,wordDict)==True:
                        memo[s]=True
                        return True
            memo[s]=False
            return False
        
        return helper(s,wordDict)
        
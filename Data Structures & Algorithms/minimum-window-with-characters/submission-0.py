class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t)>len(s):
            return ""
        need=Counter(t)
        have=Counter()
        required=len(need)
        formed=0
        left=0
        best_len=float("inf")
        best_left=0
        for right,char in enumerate(s):
            have[char]+=1
            if char in need and have[char]==need[char]:
                formed+=1
            
            while formed==required:
                if right-left+1<best_len:
                    best_len=right-left +1
                    best_left=left
                have[s[left]]-=1
                if s[left] in need and have[s[left]]<need[s[left]]:
                    formed-=1
                left+=1

        if best_len==float("inf"):
            return ""
        else:
            return s[best_left:best_left+best_len]



        



        
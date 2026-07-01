class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        elif len(s)<2:
            return 1
        else:
            i,j=0,0
            max_count=float("-inf")
            for i in range(len(s)):
                j=i+1
                current=[s[i]]
                while j<=len(s)-1:
                    if s[j] not in current:
                        current.append(s[j])
                        j+=1
                    else:
                        break
                max_count=max(max_count,len(current))
            return max_count


        
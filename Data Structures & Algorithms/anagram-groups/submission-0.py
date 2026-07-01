class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for word in strs:
            c=''.join(sorted(word))
            if c not in groups:
                groups[c]=[word]
            else:
                groups[c].append(word)
        return list(groups.values())


        
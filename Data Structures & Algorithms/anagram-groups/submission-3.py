class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master={}
        for s in strs:
            freq=[0]*26
            for c in s:
                b=ord(c)-ord('a')
                freq[b]+=1
            if tuple(freq) not in master:
                master[tuple(freq)]=[]
            master[tuple(freq)].append(s)
        return [item for item in master.values()]

        
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def dfs(i,curr,total):
            if total==target:
                res.append(curr.copy())
                return
            if i>len(candidates)-1 or total>target:
                return
            curr.append(candidates[i])
            dfs(i+1,curr,candidates[i]+total)
            curr.pop()
            j=i+1
            while j < len(candidates) and candidates[j]==candidates[i]:
                j+=1
            dfs(j,curr,total)
        dfs(0,[],0)
        return res
            
        
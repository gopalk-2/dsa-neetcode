class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo={}
        def dfs(target,index):
            if (target,index) in memo:
                return memo[(target,index)]
            if target==0:
                return 1
            if target <0:
                return 0
            count=0
            for i in range(index,len(coins)):
                coin=coins[i]
                count+=dfs(target-coin,i)
            memo[(target,index)]=count
            return count
        return dfs(amount,0)    
            

        
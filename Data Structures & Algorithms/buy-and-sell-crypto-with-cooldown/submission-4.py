class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        def dfs(i,buy):
            if (i,buy) in memo:
                return memo[(i,buy)]
            if i>=len(prices):
                return 0
            if buy:
                buy_profit=dfs(i+1,False)-prices[i]
                cooldown=dfs(i+1,True)
                memo[(i,buy)]=max(buy_profit,cooldown)
            else:
                sell=dfs(i+2,True)+prices[i]
                cooldown=dfs(i+1,False)
                memo[(i,buy)]=max(sell,cooldown)
            return memo[(i,buy)]
        return dfs(0,True)
        
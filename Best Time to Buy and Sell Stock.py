class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        mini_cost=prices[0]
        for i in range(len(prices)):
            cost=prices[i]-mini_cost
            profit=max(profit,cost)
            mini_cost=min(mini_cost,prices[i])
        return profit
            

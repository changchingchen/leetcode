class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        profit = 0
        can_buy = True
        buy_price = 0

        for i in range(len(prices) - 1):
            if can_buy and prices[i+1] > prices[i]:
                buy_price = prices[i]
                can_buy = False
            elif not can_buy and prices[i+1] < prices[i]:
                profit += (prices[i] - buy_price)
                can_buy = True

        if not can_buy and prices[-1] > buy_price:
            profit += (prices[-1] - buy_price)

        return profit
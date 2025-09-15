def maxProfit(self, prices: List[int]) -> int:
        minprice=float('inf')
        profit=0
        for i in prices:
            if minprice>i:
                minprice=i
            elif i-minprice>profit:
                profit=i-minprice
        return profit
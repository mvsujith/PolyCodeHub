prices=[1,2]
def maxProfit(prices):
        buy=prices[0]
        maxprofit=0
        for i in range(1,len(prices)-1):
            if prices[i]<buy:
                buy=prices[i]
            else:
                maxprofit=max(maxprofit,prices[i]-buy)                
        return maxprofit
print(maxProfit(prices))

"""prices=[1,2]
def maxProfit(prices):
        currentmax=0
        maxprofit=0
        for i in range(1,len(prices)):
                currentmax=prices[i]-prices[i-1]
                currentmax=max(0,currentmax)
                maxprofit=max(maxprofit,currentmax)                
                                               
        return maxprofit
print(maxProfit(prices))"""


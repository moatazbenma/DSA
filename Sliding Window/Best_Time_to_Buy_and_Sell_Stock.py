def examp():
    prices = [3,2,6,5,0,3]

    buy, sell = 0, 1
    maxP = 0

    while sell < len(prices):
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            maxP = max(maxP, profit) 
        else:
            buy += 1
        sell += 1
    print(maxP)

examp()
def examp():

    prices = [7,1,5,3,6,4]

    seen = 0
    left = 0
    right = len(prices)

    while left < right: 
        
        current = prices[left]

        if current < seen:
            seen = current
            

        if prices[left] > prices[right]:
            left = left + 1
        

examp()
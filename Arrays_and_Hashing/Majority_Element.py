from collections import Counter


#Boyer–Moore string-search algorithm


def Majority():
    count = 0
    candidate = 0

    nums = [1,2,2,2,1,2,2]

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
        

        
    print(candidate)


Majority()
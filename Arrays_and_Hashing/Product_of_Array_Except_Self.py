import math

def examp():
    nums = [1, 2, 3, 4] 


    dicta = {}
    result = []

    for i in range(len(nums)):

        dicta.setdefault(i, [])
        
        for j in range(len(nums)):
            if j != i:
                dicta[i].append(nums[j])

    for value in dicta.values():
        result.append(math.prod(value))

    print(result)

examp()
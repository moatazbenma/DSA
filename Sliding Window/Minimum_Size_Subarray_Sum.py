def examp():
    nums = [2,3,1,2,4,3]
    target = 7


    left = 0
    min_len = float('inf')
    freq = 0


    for right in range(len(nums)):
        freq += nums[right]




        while freq >= target:

            
            min_len = min(min_len, right - left + 1)

            freq -= nums[left]

            left += 1



            


    print(0 if min_len == float('inf') else min_len)

examp()
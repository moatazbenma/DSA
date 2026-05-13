def examp():

    nums = [10,5,2,6]
    k = 100
    

    left = 0
    freq = 1
    count = 0


    for right in range(len(nums)):
        freq *= nums[right]

        if k <= 1:
            break


        while freq >= k:
            
            freq //= nums[left]

            left += 1

        count += right - left + 1
        


    print(count)





examp()
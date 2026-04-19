def examp():

    nums = [-4,-1,0,3,10]

    left = 0
    right = len(nums) - 1

    result = [0] * len(nums)

    pos = len(nums) - 1


    while left <= right:

        if nums[left] * nums[left] < nums[right] * nums[right]:
            result[pos] = nums[right] * nums[right]
            right = right - 1
        else:
            result[pos] = nums[left] * nums[left]
            left = left + 1

        pos = pos - 1



    print(result)
        

            



examp()
def examp():

    nums = [2,3,4]
    target = 6


    left = 0
    right = len(nums) - 1

    
    while left < right:
        if nums[left] + nums[right] > target:
            right = right - 1
        elif nums[left] + nums[right] < target:
            left = left + 1
        else:
            print([left + 1 , right + 1])
            break

examp()
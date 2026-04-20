def examp():
    nums = [0,1,0,3,12]

    left = 0
    right = 0



    for right in range(len(nums)):
        if nums[right] != 0:
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp 
            
            left = left + 1
        
    print(nums)


examp()
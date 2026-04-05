def examp():


    nums = [1,1,2]


    slow = 0
    
    if not nums:
        return 0


    for fast in range(len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]


        

    print(slow + 1)


examp()
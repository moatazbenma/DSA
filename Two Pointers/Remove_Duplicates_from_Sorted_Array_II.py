def examp():


    nums = [0,0,1,1,1,1,2,3,3]


    slow = 0
    keep = 0
    if not nums:
        return 0


    for fast in range(len(nums)):

        if slow < 2 or nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1

            
        else:
            continue
        


        
        

        
    
        
    print(slow)
    print(nums)


examp()
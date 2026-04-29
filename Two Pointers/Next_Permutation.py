def examp():


    nums = [2,3,1]

   
    for i in range(len(nums) - 2, -1, -1):
        for j in range(len(nums) - 1, i, -1):

            if nums[j] > nums[i]:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                nums[i+1:] = reversed(nums[i+1:])
                print(nums)
                return

            
                
    # edge case (no i found)
    nums.reverse()
    print(nums)    
                



examp()
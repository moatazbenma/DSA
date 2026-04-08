def examp():

    nums = [-1,0,1,2,-1,-4]

    nums.sort()

    left = 0
    right = len(nums) - 1
    search = 1
    
    elements = []


    for search in range(0, nums - 2):
        if nums[search] + (nums[left] + nums[right]) == 0:
            elements.append([nums[search], nums[left], nums[right]])
            left += 1
            right -= 1

            
        search += 1 


    print(elements)
    print(nums)


examp()
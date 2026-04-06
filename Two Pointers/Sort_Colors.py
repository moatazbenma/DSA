def examp():
    nums = [2,0,2,1,1,0]


    left = 0
    right = len(nums) - 1
    mid = 0

    while mid <= right:
        if nums[mid] == 1:
            mid += 1
            
        elif nums[mid] == 0:
            temp = nums[mid]
            nums[mid] = nums[left]
            nums[left] = temp

            

            mid += 1
            left += 1

        else:
            temp = nums[mid]
            nums[mid] = nums[right]
            nums[right] = temp

            right -= 1


    print(nums)

examp()
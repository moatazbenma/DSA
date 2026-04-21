def examp():
    nums = [3,2,2,3]
    val = 3

    
    left = 0


    for right in range(len(nums)):
        if nums[right] != val:
            nums[left] = nums[right]

            left = left + 1
        else:
            pass


    print(left)


examp()



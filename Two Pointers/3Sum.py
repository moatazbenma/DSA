def examp():

    nums = [-1,0,1,2,-1,-4]

    nums.sort()



    
    elements = []


    for search in range(len(nums) - 2):
        left = search + 1
        right = len(nums) - 1

        if search > 0 and nums[search] == nums[search - 1]:
                continue

        while left < right:


            if nums[search] + (nums[left] + nums[right]) < 0:
                left += 1

            elif nums[search] + (nums[left] + nums[right]) > 0:
                right -= 1


            else:

                triplet = [nums[search], nums[left], nums[right]]


                elements.append(triplet)
                right -= 1 
                left += 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1


    print(elements)
    print(nums)


examp()
def examp():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3

    nums2 = [2, 5, 6]
    n = 3

    left = m - 1
    right = len(nums1) - 1
    nums2_right = len(nums2) - 1


    while nums2_right >= 0:

        if left >= 0 and nums1[left] > nums2[nums2_right]:
            nums1[right] = nums1[left]
            left -= 1

        else:
            nums1[right] = nums2[nums2_right]
            nums2_right = nums2_right - 1


        right = right - 1


    print(left)
    print(nums1)


examp()
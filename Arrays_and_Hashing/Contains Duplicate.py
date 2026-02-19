from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False

# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 1]
    print(sol.containsDuplicate(nums))  # Output: True

    nums2 = [1, 2, 3, 4]
    print(sol.containsDuplicate(nums2))  # Output: False

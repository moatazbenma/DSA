from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Example usage
if __name__ == "__main__":
    sol = Solution()

    print(sol.isAnagram("listen", "silent"))  # Output: True
    print(sol.isAnagram("hello", "bello"))    # Output: False

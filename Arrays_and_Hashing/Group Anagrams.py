from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word not in words:
                words[sorted_word] = []
            words[sorted_word].append(word)

        return list(words.values())

# Example usage
if __name__ == "__main__":
    sol = Solution()
    input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = sol.groupAnagrams(input_words)
    print(result)
    # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

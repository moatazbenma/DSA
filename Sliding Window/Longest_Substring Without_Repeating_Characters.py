from collections import Counter

def examp():
    s = "abcabcbb"
    counts = {}

    left = 0
    max_len = 0


    for right in range(len(s)):
        char = s[right]

        counts[char] = counts.get(char, 0) + 1

        while counts[char] > 1:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    print(max_len)




examp()

        




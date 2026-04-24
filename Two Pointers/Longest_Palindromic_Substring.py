def examp():
    s = "abba"
    longest = ""

    for i in range(len(s)):

        # odd
        left = i - 1
        right = i + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        candidate1 = s[left+1:right]

        if len(candidate1) > len(longest):
            longest = candidate1

        # even
        lefta = i
        righta = i + 1

        while lefta >= 0 and righta < len(s) and s[lefta] == s[righta]:
            lefta -= 1
            righta += 1

        candidate2 = s[lefta+1:righta]

        if len(candidate2) > len(longest):
            longest = candidate2

    print(longest)

examp()
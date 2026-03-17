from collections import Counter

def examp():
    s = "cbaebabacd"
    p = "abc"

    p_count = Counter(p)
    window = Counter()
    result = []

    left = 0

    for right in range(len(s)):
        window[s[right]] += 1

        if right - left + 1 > len(p):
            window[s[left]] -= 1

            if window[s[left]] == 0:
                del window[s[left]]
            left += 1

        if window == p_count:
            result.append(left)

            


    print(result)

examp()
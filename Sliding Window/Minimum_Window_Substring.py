def examp():
    s = "ADOBECODEBANC"
    t = "ABC"



    t_freq = {}

    for char in t:
        if char not in t_freq:
            t_freq[char] = 0
        t_freq[char] += 1


    left = 0
    count = {}
    min_count = float('inf')


    for right in range(len(s)):


        if s[right] in t:
            if s[right] not in count:
                count[s[right]] = 0
            count[s[right]] += 1

        while count.keys() == t_freq.keys():
            min_count = min(min_count, (right - left + 1))
            
            if s[left] in count:
                if s[left] not in count:
                    count[s[left]] = 0
                count[s[left]] += 1
            count[s[left]] -= 1
 

    print(count)
    print(min_count)

 

examp()
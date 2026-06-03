def examp():
    s = "a"
    t = "aa"



    t_freq = {}

    for char in t:
        if char not in t_freq:
            t_freq[char] = 0
        t_freq[char] += 1


    left = 0
    count = {}
    min_count = float('inf')
    start_index  = 0
    last_index = 0
    current_length = 0

    for right in range(len(s)):


        if s[right] in t:
            if s[right] not in count:
                count[s[right]] = 0
            count[s[right]] += 1

        while all(count.get(char, 0) >= t_freq[char] for char in t_freq):
            current_length = right - left + 1

            if current_length < min_count:
                min_count = current_length
                start_index = left
                last_index = right
            
            if s[left] in count:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
            left += 1


    if min_count == float('inf'):
        print("")
    else:
        s[start_index:last_index+1]

 

examp()
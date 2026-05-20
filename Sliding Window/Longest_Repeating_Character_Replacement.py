def examp():

    s = "AABABBA"
    k = 1
    
    count = {}

    best_window = 0

    left = 0
    for right in range(len(s)):
        if s[right] not in count:
            count[s[right]] = 0
        count[s[right]] += 1
        

        while (right - left + 1) - max(count.values()) > k:
            count[s[left]] -= 1
            left += 1

        best_window = max(best_window, (right - left + 1))


    print(best_window)
        
    
  

examp()
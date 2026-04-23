def examp():
    s = "racecarxyz"





    
    for i in range(1, len(s) - 1):
        left = i - 1
        right = i + 1

        while left >= 0  and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1


        print(s[left + 1:right])



        




examp()
        
def examp():


    s = "axc"
    t = "ahbgdc"


    right = 0

    left = 0

    for right in range(len(t)):

        if left == len(s):
            break

        if t[right] == s[left]:
            left = left + 1

    if left == len(s):
        print("true")
    else:
        print("false")
        
    



        
examp()
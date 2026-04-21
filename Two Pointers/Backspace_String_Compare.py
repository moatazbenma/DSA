def examp():
    t = "b"
    s = "a#c"




    
    result = ""
    left_t = ""
    
    for right in range(len(s)):


        if s[right] == "#":
            result = result[:-1] 
  
        else:
            result += s[right]

    for left in range(len(t)):



        if t[left] == "#":
            left_t = left_t[:-1] 
  
        else:
            left_t += t[left]


    if left_t == result:
        print("true")
    else:
        print("false")

    print(result)
    print(left_t)

examp()
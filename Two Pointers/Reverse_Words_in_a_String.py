def examp():

    s = "the sky is blue"

    new_s = list(s)


    left = 0
    right = len(new_s) - 1


    while left < right:
        temp = new_s[left]
        new_s[left] = new_s[right]
        new_s[right] = temp

        left += 1
        right -= 1

    print(new_s)


    start = 0
    end = 0
    for i in range(len(new_s)):
        

        if new_s[i] == " ":
            end = i - 1


            while start < end:
                temp = new_s[start]
                new_s[start] = new_s[end]
                new_s[end] = temp

                start += 1
                end -= 1

        elif i == len(new_s) - 1:

            end = len(new_s) - 1
            
            while start < end:
                temp = new_s[start]
                new_s[start] = new_s[end]
                new_s[end] = temp

                start += 1
                end -= 1
                

        
        else:
            continue

        start = i + 1
        end = i


        

    result = "".join(new_s)
    print(" ".join(result.split()))

        

examp()
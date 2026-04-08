def examp():
    height = [1,8,6,2,5,4,8,3,7]


    start  = 0
    end = len(height) - 1
    current = 0

    sir = set()



    seen = 0
    current = 0

    while start < end:
        index = end - start



        area = index * min(height[start], height[end])
        current = area

        if current > seen:
            seen = current
 

        if height[start] < height[end]:
            start = start + 1


            
        elif height[start] > height[end]:
            end = end - 1
        
        else:
            left += 1

    print(seen)
            
examp()
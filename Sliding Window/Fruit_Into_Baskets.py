def examp():
    fruits = [1,2,3,2,2]

    counts = {}
    max_count = 0

    left = 0
    for right in range(len(fruits)):
        if fruits[right] not in counts:
            counts[fruits[right]] = 0
        counts[fruits[right]] += 1

        while len(counts) > 2:
            counts[fruits[left]] -= 1
            if counts[fruits[left]] == 0:
                del counts[fruits[left]]

            left += 1


        max_count = max(max_count, (right - left + 1))



    print(max_count)


examp()
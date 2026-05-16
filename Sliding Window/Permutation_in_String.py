def examp():

    s1 = "ab"
    s2 = "eidbaooo"

    dic_s1 = {}


    k = len(s1)


    for char in s1:
        if char not in dic_s1:
            dic_s1[char] = 0
        dic_s1[char] += 1

    dic_s2 = {}


    for char in s2[:k]:
        if char not in dic_s2:
            dic_s2[char] = 0
        dic_s2[char] += 1

    if dic_s1 == dic_s2:
        print('true')


    for i in range(k, len(s2)):
        dic_s2[s2[i - k]] -= 1

        if dic_s2[s2[i - k]] == 0:
            del dic_s2[s2[i - k]]

        if s2[i] not in dic_s2:
            dic_s2[s2[i]] = 0

        dic_s2[s2[i]] += 1

        if dic_s2 == dic_s1:
            print("True")
            break



examp()
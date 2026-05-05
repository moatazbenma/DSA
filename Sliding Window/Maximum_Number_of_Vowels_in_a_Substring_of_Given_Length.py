
def examp():
    s = "abciiidef"
    k = 3

    vowels = set("aeiou")

    freq = 0
    max_freq = freq

    for i in range(k):
        if s[i] in vowels:
            freq += 1

    for i in range(k, len(s)):   


        if s[i - k] in vowels:
            freq -= 1

        if s[i] in vowels:
            freq += 1

        max_freq = max(max_freq, freq)




    print(max_freq)



examp()
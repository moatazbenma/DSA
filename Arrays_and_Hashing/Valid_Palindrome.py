import re
def examp():

    s = "A man, a plan, a canal: Panamz"

    s = re.sub("[^a-zA-Z0-9]", "", s).lower()


    n = len(s)
    for i in range(n // 2):
        if(s[i] != s[n - i - 1]):
            print(False)
            return
            
    
    print(True)


examp()
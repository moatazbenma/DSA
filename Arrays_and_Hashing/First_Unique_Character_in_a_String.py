
s = 'loveleetcode'

res = {}

for char in s:
    if char in res:
        res[char] += 1
    else:
        res[char] = 1
        
        
for i, char in enumerate(s):
    if res[char] == 1:
        print(i)
        break
else:
    print(-1)
    

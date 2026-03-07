from collections import Counter

def example():
    nums = [3, 0, 1, 0]
    k = 1
    result = dict(Counter(nums).most_common(k))
    lista = []

    
    for key in result:
        lista.append(key)
        
    print(lista)

example()




strings = ['Some string', 'Art', 'Music', 'Artificial Intelligence']
print([x.lower() for x in strings if len(x) > 5])

def quicksort(m) :
    # m is a list of numbers
    if len(m) < 2:
        return m
    lesser = [x for x in m if x < m[0]]
    greater = [x for x in m[1:] if x >= m[0]]
    return (quicksort(lesser) +[m[0]]+ quicksort(greater)) 

print(quicksort([3,7,9,5,3,6,8,9]))

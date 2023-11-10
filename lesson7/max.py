def large(f): 
    max_ = f[0] 
    for m in f: 
        if m > max_:
             max_ = m
    return max_ 
list1 = [1,4,5,2,6] 
result = large(list1) 
print(result) 
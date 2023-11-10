
def sum(*args):
    result = 0
    for arg in args:
        result =+ arg
        return result
        
grades1 = [95]
grades2 = [88]
grades3 = [75]
grades4 = [92]
grades5 = [78]

print(sum(*grades1 , *grades2, *grades3, *grades4, *grades5))
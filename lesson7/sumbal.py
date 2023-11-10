def  sum(student, *args):
    print(f '')
    for arg in args:
        result += arg
    return result
grades = (95,88,75,92,78)
print(sum(*grades))
def find_max(arr , max = None):
    if max is None:
        max = arr.pop()
    current =arr.pop()
    if current > max:
        max = current
    if arr:
        return find_max(arr, max)  
    return max
list = [5,9,23,40,55]
result = find_max(list)
print(result)
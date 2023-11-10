nums = [6, 2, 88, 23, 0, -5, 30, 9, 20, 10, 6, 56, -7]

num3=[]
num5=[]
for num in nums:
    if num == 0:
        continue
    if num % 3 == 0:
        num3.append(num)
    if num % 5 == 0:
        num5.append(num)       

print(num3)
print(num5)
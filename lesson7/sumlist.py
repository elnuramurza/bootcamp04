#naiti summy cisel v spiske
#1 
nums = [5,'test', 8, "None", 32, False, 6, 42, 3.4, 52, "hi"] #...
s = 0
for n in nums:
    if isinstance(n,(int, float)):
        s += n
print(s)
#2
num_1 =[5, 8, 32, 6, 42, 3.4, 52] 
print(sum(num_1))       
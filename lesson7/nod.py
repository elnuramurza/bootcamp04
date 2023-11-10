#spisok cisel ot1 don,
#naiti prosty cisla
n =100000
nums = list(range(n+1)) #[0, 1, 2, 3, 4]
for k in range(2, n+1): #2
    for m in range(2*k, n+1, k): #2
        nums[m]=0

for p in nums:
    if p > 0:
        print(p)

#1
#for i in range(1, n + 1): #8
#    need_to_break = false
#    for j in range(2, i);
#        if i % J == 0: # true
#            need_to_break = true
#            break
#    if not need_to_break:
#         print(i)       
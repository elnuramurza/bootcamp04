k = 100000
def lucky(num):
    for i in range (1, k):
        if i == num:
            print(i, "verno")
            break

def binary_search(num):
    q = 0
    c = int(k / 2)
    step = c / 2
    while True:
        print(c)
        if c < num:
            print("menshe")
            c = rount(c + step)
        elif c > num:
            print("bolshe")
            c = rount(c - step)
        else:
            print(c, f"verno! kolicestvo shagov {q}")
            break
        step /= 2
        q += 1

n = int(input(f"vedite cislo ot 1 do {k}: "))
#lucky(n)
binary_search(n)
     
        
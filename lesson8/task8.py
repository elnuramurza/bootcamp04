def f_hanoi(n, A,C):
    if n <=0:
        return
    B = 6 - A - C
    f_hanoi(n-1, A,B)
    print(f"peremestit disk {n} so shytrka {A} na shytrek {C} ")  
    f_hanoi(n -1, B, C)
f_hanoi(5,1,3)  
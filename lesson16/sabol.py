def noxojdenie_samogo_bolshogo_prostogo_delitel(n):
    delitel = 2
    while n > 1:
        if n % delitel == 0:
            n /= delitel
        else:
            delitel += 1
    return delitel

chislo = 600851475143
samyi_bolshoi_prostoi_delitel = noxojdenie_samogo_bolshogo_prostogo_delitel (chislo)
print(samyi_bolshoi_prostoi_delitel)

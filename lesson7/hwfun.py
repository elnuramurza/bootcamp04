
def power(base, exponent): 
    m = 1000 
    result = [0] * m
    result[-1] = base 
    c = 1 
    for _ in range(1, exponent): 
        carry = 0 
        for position in range(m - 1, m - c - 1, -1): 
            product = result[position] * base + carry 
            result[position] = product % 10 
            carry = product // 10 
        if carry > 0: 
            c += 1 
            result[m - c] = carry

    return result[m - c:]

print(power(2, 15)) 
print(''.join(map(str, power(2, 15))))
print(sum(power(2, 15))) 
print(power(2, 1000)) 
print(''.join(map(str, power(2, 1000))))
print(sum(power(2, 1000)))



















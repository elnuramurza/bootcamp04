def generate_even_numbers(n):
    even_numbers = [x for x in range(1, n + 1) if x % 2 == 0]
    return even_numbers
n = 80
even_numbers=generate_even_numbers(n)   
print(even_numbers) 
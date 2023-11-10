even_numbers =[]
odd_numbers =[]
even_cubes =[]

for i in range (1, 51):
    if i % 2 == 0:  
        even_numbers.append(i)
        even_cubes.append(i ** 3)
    else:
        odd_numbers.append(i)
print(even_numbers)
print(odd_numbers)
print(even_cubes)


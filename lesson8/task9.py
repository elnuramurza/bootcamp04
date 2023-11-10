numbers = list(range(5, 61, 5))
if 20 in numbers:
    index_20 = numbers.index(20)
    numbers[index_20] = 200
sum_of_numbers = sum(numbers)
print("summa vsex elementov spiska:", sum_of_numbers)

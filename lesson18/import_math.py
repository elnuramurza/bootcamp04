import math

result_cos_pi = math.cos(math.pi)
result_sqrt_e = math.sqrt(math.e)
result_factorial_5 = math.factorial(5)

print("cos(π):", result_cos_pi)
print("√e:", result_sqrt_e)
print("5!:", result_factorial_5)



from datetime import datetime

current_time = datetime.now().time()
print("Текущее время:", current_time)



import random as rnd

li = [rnd.randint(1, 20) for _ in range(5)]
random_element = rnd.choice(li)

print("Список:", li)
print("Случайный элемент из списка:", random_element)



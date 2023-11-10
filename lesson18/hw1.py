from random import randrange

random_number = randrange(10)
attempts = 0

while True:
    user_input = input("Введите число от 0 до 9: ")
    
    try:
        user_guess = int(user_input)
        if 0 <= user_guess <= 9:
            attempts += 1
            if user_guess == random_number:
                print(f"Поздравляем! Вы угадали число {random_number} с {attempts} попытки.")
                break
            else:
                print("Попробуйте ещё раз.")
        else:
            print("Введите число в диапазоне от 0 до 9.")
    except ValueError:
        print("Введите целое число от 0 до 9.")

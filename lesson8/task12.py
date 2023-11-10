name = input("Введите имя: ") 
surname = input("Введите фамилию: ") 
plate = input("Введите номерной знак: ") 
if len(plate) == 7 and plate[1:5].isdigit() and plate[0].isalpha() and plate[5:].isalpha() and len(plate[5:]) <= 2:
     plate_type = "старый образец" 
elif len(plate) == 6 and plate[:3].isdigit() and plate[3:].isalpha() and len(plate[3:]) == 3: plate_type = "новый образец" 
else: 
    print("Ошибка: номерной знак не соответствует ни старому, ни новому образцу.") 
    exit() 
    print(f"{name} {surname}, номерной знак {plate}, у вас {plate_type}.")
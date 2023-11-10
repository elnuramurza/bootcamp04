from openpyxl import load_workbook

file_name = "students1.xlsx"
excel = load_workbook(file_name)
page = excel["Лист1"]

commands = {
    "1": "Показать студентов",
    "2": "Показать оценки",
    "3": "Средняя оценка"
}

# ввод
print("Выберите команду:")
for key, value in commands.items():
    print(key, value)
input_value = input()

# обработка и вывод
# "Показать студентов"
if input_value == "1":
    for cell in page["A"]:
        if cell.row == 1:
            continue
        print(cell.value)

# Показать оценки
elif input_value == "2":
    for cell in page["B"]:
        if cell.row == 1:
            continue
        print(cell.value)

# Средняя оценка
elif input_value == "3":
    # 1
    sm = 0
    qty = 0
    for cell in page["B"]:
        if cell.row == 1:
            continue
        sm += cell.value
        qty += 1
    print(sm / qty)
    # 2
    marks = [cell.value for cell in page["B"] if cell.row != 1]
    print(sum(marks) / len(marks))

 

import requests

url = "https://api.telegram.org/bot6450383163:AAHb6Do-tMkORRBWdQjAyZrXyWyq1-1teC0/"

# получение обновлений (последние сообщения)
# response = requests.get(f"{url}getUpdates")
# data = response.json()
# print(data["result"][-1]["message"]["text"])

# отправка сообщений
chat_id = 6681383056
text = "Привет, Эльдияр!"
requests.get(f"{url}sendMessage?chat_id={chat_id}&text={text}")

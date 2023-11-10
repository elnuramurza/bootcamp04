import requests
from openpyxl import Workbook
server_response = requests.get("https://jsonplaceholder.typicode.com/posts")
date = server_response.json()
names = []
for element in date:
    names.append(element["name"])
new_exsel_file = Workbook()
page = new_exsel_file.active
for name in names:
    page.append([name])
new_exsel_file.save("users_table.xlsx")    

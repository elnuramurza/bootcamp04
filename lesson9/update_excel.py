from openpyxl import load_workbook
excel_file = load_workbook("users_table.xlsx")
page = excel_file["Sheet"]
#ctenie
print(page["A7"].value)
#dobavlenie
page["A11"] = "Janar Ailciev"
excel_file.save("users_table.xlsx")
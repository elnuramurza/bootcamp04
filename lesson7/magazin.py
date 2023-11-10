print("Добро пожаловать в магазин!")
products = {
    "apple": {"цена": 1.0, "количество": 100},
    "banan": {"цена": 0.5, "количество": 50},
    "orange": {"цена": 1.2, "количество": 70}
}

while True:
    product_name = input('vvedite product dlz vyxoda naberite escape').lower()

    if product_name == "escape":
        break

    if product_name in products:
        print(products[product_name])
        print("next product")
    else:
        print("takogo net")
print("Спасибо за покупки! До свидания!")

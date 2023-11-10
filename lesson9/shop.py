class Shop:
    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_product(self, product_name, price, quantity=1):
        if product_name in self.products:
            self.products[product_name] = (price, self.products[product_name][1] + quantity)
        else:
            self.products[product_name] = (price, quantity)
        print(f"product '{product_name}' added to the store'{self.name}' by price {price}.")

    def get_product_info(self, product_name):
        if product_name in self.products:
            return self.products[product_name]
        else:
            return None

    def buy_product(self, product_name, quantity):
        if product_name in self.products:
            price, available_quantity = self.products[product_name]
            if available_quantity >= quantity:
                total_cost = price * quantity
                self.products[product_name] = (price, available_quantity - quantity)
                print(f"you bought {quantity} pieces product '{product_name}' for total cost {total_cost}.")
            else:
                print(f"Sorry, no goods '{product_name}' not enough in the store.")
        else:
            print(f"Sorry, no goods'{product_name}' not in store.")

my_shop = Shop("My store")

my_shop.add_product("Milk", 2, 10)
my_shop.add_product("Bread", 1.5, 20)
my_shop.add_product("Egg", 3)

my_shop.buy_product("Milk", 3)
my_shop.buy_product("Bread", 25)



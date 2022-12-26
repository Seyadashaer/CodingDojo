
class Product: 
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += percent_change * self.price
        else:
            self.price -= percent_change * self.price
        return self

    def print_info(self):
        print("Name of the product:", self.name,",The category of the Product:", self.category, ",The price of the Product is:", self.price)

class Store:
    def __init__(self, name, products_list=[]):
        self.name = name
        self.products_list = products_list
        self.product = Product(name, price=100, category="A")

    def add_product(self, new_product):
        self.products_list.append(new_product)

    def sell_product(self, id):
        del self.products_list[id]

    def inflation(self):
        self.product.update_price(percent_change=.02, is_increased=True)
        print(self.product.price)





makeup = Product("makeup", 30, "Beauty")
makeup.update_price(.3, True)
makeup.print_info()

lineStore = Store("Line Store", ["Hats", "Nails"])
lineStore.add_product("makeup")
print(lineStore.products_list)

lineStore.sell_product(0)
lineStore.inflation()
print(lineStore.products_list)

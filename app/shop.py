import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products
        self.each_product_cost = {}
        self.total_cost = 0

    def purchase(self, product_cart: dict) -> int:
        for product in product_cart:
            product_cost = product_cart[product] * self.products[product]
            if product_cost.is_integer():
                product_cost = int(product_cost)
            self.each_product_cost[product] = product_cost
            self.total_cost += product_cost
        return self.total_cost

    def receipt(self, customer_name: str, product_cart: dict) -> None:
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_time}\nThanks, "
              f"{customer_name}, for your purchase!")
        print("You have bought:")
        for product in self.each_product_cost:
            print(f"{product_cart[product]} {product}s "
                  f"for {self.each_product_cost[product]} dollars")
        print(f"Total cost is {self.total_cost} dollars\nSee you again!\n")

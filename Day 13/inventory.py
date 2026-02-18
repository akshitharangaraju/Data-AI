import json
from datetime import datetime

# ------------------------------
# DECORATOR FOR LOGGING
# ------------------------------
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {datetime.now()} -> Executing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# ------------------------------
# BASE CLASS: PRODUCT
# ------------------------------
class Product:
    def __init__(self, pid, name, price, stock):
        self.__pid = pid
        self.__name = name
        self.__price = price
        self.__stock = stock

    # Getters
    def get_id(self):
        return self.__pid

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    # Setter
    def set_stock(self, value):
        if value >= 0:
            self.__stock = value
        else:
            raise ValueError("Stock cannot be negative")

    # Polymorphism (to be overridden)
    def display(self):
        return {
            "id": self.__pid,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "type": "Product"
        }


# ------------------------------
# SUBCLASS: ELECTRONICS
# ------------------------------
class Electronics(Product):
    def __init__(self, pid, name, price, stock, warranty):
        super().__init__(pid, name, price, stock)
        self.warranty = warranty

    def display(self):
        data = super().display()
        data["type"] = "Electronics"
        data["warranty"] = self.warranty
        return data


# ------------------------------
# SUBCLASS: GROCERY
# ------------------------------
class Grocery(Product):
    def __init__(self, pid, name, price, stock, expiry):
        super().__init__(pid, name, price, stock)
        self.expiry = expiry

    def display(self):
        data = super().display()
        data["type"] = "Grocery"
        data["expiry"] = self.expiry
        return data


# ------------------------------
# CUSTOM ITERATOR
# ------------------------------
class InventoryIterator:
    def __init__(self, products):
        self._products = products
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._products):
            raise StopIteration
        item = self._products[self._index]
        self._index += 1
        return item


# ------------------------------
# INVENTORY MANAGER
# ------------------------------
class Inventory:
    def __init__(self):
        self.products = []

    @logger
    def add_product(self, product):
        self.products.append(product)
        print("Product added successfully.")

    @logger
    def remove_product(self, pid):
        for p in self.products:
            if p.get_id() == pid:
                self.products.remove(p)
                print("Product removed.")
                return
        print("Product not found.")

    @logger
    def update_stock(self, pid, new_stock):
        for p in self.products:
            if p.get_id() == pid:
                p.set_stock(new_stock)
                print("Stock updated.")
                return
        print("Product not found.")

    def search(self, keyword):
        results = []
        for p in self.products:
            if keyword.lower() in p.get_name().lower():
                results.append(p.display())
        return results

    def show_all(self):
        for p in InventoryIterator(self.products):
            print(p.display())

    @logger
    def save(self, filename="inventory.json"):
        data = [p.display() for p in self.products]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Inventory saved.")

    @logger
    def load(self, filename="inventory.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            self.products.clear()

            for item in data:
                if item["type"] == "Electronics":
                    obj = Electronics(item["id"], item["name"], item["price"],
                                      item["stock"], item["warranty"])
                elif item["type"] == "Grocery":
                    obj = Grocery(item["id"], item["name"], item["price"],
                                  item["stock"], item["expiry"])
                else:
                    obj = Product(item["id"], item["name"],
                                  item["price"], item["stock"])
                self.products.append(obj)

            print("Inventory loaded.")

        except FileNotFoundError:
            print("File not found.")


# ------------------------------
# MENU SYSTEM
# ------------------------------
def main():
    inv = Inventory()

    while True:
        print("\n===== Inventory Menu =====")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Show All")
        print("6. Save")
        print("7. Load")
        print("8. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                pid = input("ID: ")
                name = input("Name: ")
                price = float(input("Price: "))
                stock = int(input("Stock: "))
                ptype = input("Type (E=Electronics, G=Grocery): ").upper()

                if ptype == "E":
                    warranty = input("Warranty (years): ")
                    product = Electronics(pid, name, price, stock, warranty)
                elif ptype == "G":
                    expiry = input("Expiry date: ")
                    product = Grocery(pid, name, price, stock, expiry)
                else:
                    product = Product(pid, name, price, stock)

                inv.add_product(product)

            elif choice == "2":
                pid = input("Enter ID: ")
                inv.remove_product(pid)

            elif choice == "3":
                pid = input("Enter ID: ")
                stock = int(input("New Stock: "))
                inv.update_stock(pid, stock)

            elif choice == "4":
                key = input("Enter name to search: ")
                results = inv.search(key)
                for r in results:
                    print(r)

            elif choice == "5":
                inv.show_all()

            elif choice == "6":
                inv.save()

            elif choice == "7":
                inv.load()

            elif choice == "8":
                print("Exiting...")
                break

            else:
                print("Invalid choice.")

        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()

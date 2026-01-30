menu = {
    1: ("Pizza", 250),
    2: ("Burger", 120),
    3: ("Biryani", 180),
    4: ("Pasta", 200),
    5: ("Cold Drink", 50)
}

GST_PERCENT = 5

promo_codes = {
    "ZOMATO50": 50,     # flat ₹50 off
    "SAVE20": 20        # flat ₹20 off
}

try:
    print("Welcome to Zomato ")
    print("\n------ MENU ------")
    for key, value in menu.items():
        print(f"{key}. {value[0]} - ₹{value[1]}")

    choice = int(input("\nEnter food number: "))
    if choice not in menu:
        raise ValueError("Invalid food choice")

    plates = int(input("Enter number of plates: "))
    if plates <= 0:
        raise ValueError("Plates must be greater than zero")

    food_name, price = menu[choice]
    subtotal = price * plates
    membership = input("Do you have Zomato Gold membership? (yes/no): ").lower()
    membership_discount = 0
    if membership == "yes":
        membership_discount = subtotal * 0.10  # 10% discount
    annual_offer = input("Is annual offer applicable? (yes/no): ").lower()
    annual_discount = 0
    if annual_offer == "yes":
        annual_discount = subtotal * 0.05  # 5% discount
    promo = input("Enter promo code (or press enter to skip): ").upper()
    promo_discount = promo_codes.get(promo, 0)
    gst_amount = subtotal * GST_PERCENT / 100
    total = subtotal + gst_amount
    total -= (membership_discount + annual_discount + promo_discount)

    if total < 0:
        total = 0

    print("\n -------- BILL --------")
    print(f"Item           : {food_name}")
    print(f"Plates         : {plates}")
    print(f"Subtotal       : ₹{subtotal:.2f}")
    print(f"GST (5%)       : ₹{gst_amount:.2f}")
    print(f"Membership Off : -₹{membership_discount:.2f}")
    print(f"Annual Offer   : -₹{annual_discount:.2f}")
    print(f"Promo Discount : -₹{promo_discount:.2f}")
    print("------------------------")
    print(f"TOTAL PAYABLE  : ₹{total:.2f}")
    print("Thank you for ordering from Zomato ")

except ValueError as ve:
    print(" Input Error:", ve)

except Exception as e:
    print(" Something went wrong:", e)

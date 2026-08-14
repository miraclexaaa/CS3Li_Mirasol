def calculate_checkout(cart_total, shipping_speed):
    cart_total = float(input("enter your cart total: "))
    print("your cart total is:", cart_total)
    shipping_speed = input("enter your shipping speed(express/overnight/standard): ")
    print("your shipping speed is:", shipping_speed)
    if shipping_speed == "express":
        cart_total = cart_total + 15
    elif shipping_speed == "overnight":
        cart_total = cart_total + 25
    elif shipping_speed == "standard":
        cart_total = cart_total + 10
    if cart_total >= 100:
        cart_total = 0
    elif cart_total < 100:
        cart_total = 10
    else:
        print("Your output is invalid.")
    cart_total = 0
    return calculate_checkout
    print(calculate_checkout())

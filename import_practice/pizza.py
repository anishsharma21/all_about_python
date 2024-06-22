def make_pizza(size, *toppings):
    toppings = [topping for topping in toppings]
    pizza = {
        'size': size,
        'toppings': toppings
    }
    print(f"Making a {size} pizza with toppings: {toppings}")
    return pizza
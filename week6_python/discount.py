#Making constant of global variable
TAX_RATE= 0.13

def apply_discount(price, percentage):
    return price - (price*percentage/100) 

def apply_tax_rate(price):
    return price + (price * TAX_RATE)

def final_price(price, discount_percentage):
    discounted_price = apply_discount(price, discount_percentage)

    return apply_tax_rate(discounted_price)

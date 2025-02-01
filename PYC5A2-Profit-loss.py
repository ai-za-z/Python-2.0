cost_price = int(input("for how much did you buy the thing: "))
selling_price = int(input("For how much did you sell it: "))


if cost_price<selling_price:
    print(f"Walah!! You get a profit of {selling_price-cost_price}")
else:
    print(f"oh no!! You get a loss of {cost_price-selling_price} ")


feedback = int(input(""))
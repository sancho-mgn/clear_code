"""было"""
def MaximumDiscount(N, price):
    price = sorted(price, reverse=True)
    return sum(price[i] for i in range(2, len(price), 3))

# print(MaximumDiscount(7, [100, 350, 500, 250, 200, 50, 400, 435, 23]))


"""стало"""
def MaximumDiscount(N, list_of_prices_goods):
    list_of_prices_goods = sorted(list_of_prices_goods, reverse=True)
    return sum(list_of_prices_goods[i] for i in range(2, len(list_of_prices_goods), 3))

# print(MaximumDiscount(7, [100, 350, 500, 250, 200, 50, 400, 435, 23]))

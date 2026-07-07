# shopSmart.py
# ------------


"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""
from __future__ import print_function
import shop

from functools import reduce


def shopSmart(orderList: list[tuple[str, float]], fruitShops: list[shop.FruitShop]):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """
    total_prices: dict[shop.FruitShop, float]  = {}

    for fruit_shop in fruitShops:
        total_prices[fruit_shop] = fruit_shop.getPriceOfOrder(orderList)

    return min(total_prices.items(), key= lambda pair: pair[1])[0] # return the FruitShop object with the lowest price.


if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orders = [('apples', 1.0), ('oranges', 3.0)]
    dir1 = {'apples': 2.0, 'oranges': 1.0}
    shop1 = shop.FruitShop('shop1', dir1)
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2', dir2)
    shops = [shop1, shop2]
    print("For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName())
    orders = [('apples', 3.0)]
    print("For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName())

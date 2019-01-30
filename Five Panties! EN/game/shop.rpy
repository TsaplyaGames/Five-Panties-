init 1 python:
    
    from math import ceil
    
    def add_item_shop(item, amount, price):
        global shop_stock
        if item not in shop_stock:
            shop_stock[item] = {'amount': amount, 'price': price}
        else:
            shop_stock[item]['amount'] += amount

    def del_item_shop(item, amount):
        global shop_stock
        if item in shop_stock and shop_stock[item]['amount'] == 1:
            del shop_stock[item]
        elif item in shop_stock and shop_stock[item]['amount'] > 1:
            shop_stock[item]['amount'] -= amount
        else:
            pass
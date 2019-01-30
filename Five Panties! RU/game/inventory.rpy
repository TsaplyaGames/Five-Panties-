init 1 python:
    
    
    
    def add_item_inv(item, amount, price):
        global inventory
        if item not in inventory:
            inventory[item] = {'amount': amount, 'price': price}
        else:
            inventory[item]['amount'] += amount

    def del_item_inv(item, amount):
        global inventory
        if item in inventory and inventory[item]['amount'] == 1:
            del inventory[item]
        elif item in inventory and inventory[item]['amount'] > 1:
            inventory[item]['amount'] -= amount
        else:
            pass

    def sell_item_inv(item, amount):
        global inventory
        if item in inventory and inventory[item]['amount'] == 1:
            inventory['Талеры']['amount'] += inventory[item]['price'] * 0.8
            del inventory[item]
        elif item in inventory and inventory[item]['amount'] > 1:
            inventory[item]['amount'] -= amount
            inventory['Талеры']['amount'] += inventory[item]['price'] * 0.8
        else:
            pass
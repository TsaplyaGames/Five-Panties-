screen inventory:

    vbox xpos 0.2 ypos 0.2:
        for keys, values in sorted(inventory.items()):
            text keys + ' ' + str(values['amount'])
            
screen shop: 

    text str(int(inventory['Талеры']['amount'])) xpos 0.2 ypos 0.1
    vbox xpos 0.01 ypos 0.2:
        text 'Купить' 
        for keys, values in sorted(shop_stock.items()):
            textbutton keys + ' ' + 'Количество' + ' ' + str(values['amount']) + ' ' + 'Цена' + ' ' + str(int(ceil(values['price'] * 1.15))): 
                if inventory['Талеры']['amount'] >= values['price']:
                    action [Function(add_item_inv, keys, 1, values['price']), Function(del_item_inv, 'Талеры', values['price'] * 1.15), Function(del_item_shop, keys, 1), Function(renpy.restart_interaction)]
                elif inventory['Талеры']['amount'] < values['price']:
                    action NullAction()
                    
    vbox xpos 0.5 ypos 0.2:
        text 'Продать' 
        for keys, values in sorted(inventory.items()):
            if keys == 'Талеры':
                pass
            else:
                textbutton keys + ' ' + 'Количество' + ' ' + str(values['amount']) + ' ' + 'Цена' + ' ' + str(int(ceil(values['price'] * 0.8))):
                    action [Function(sell_item_inv, keys, 1), Function(add_item_shop, keys, values['amount'], values['price']), Function(renpy.restart_interaction)]    
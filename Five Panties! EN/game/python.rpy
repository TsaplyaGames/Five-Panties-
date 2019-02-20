init 1 python: 
    mp = MultiPersistent('fivepanties!')
    
label load_stuff:
    $ inventory = {}
    $ add_item_inv('Талеры', 50, 1)
    $ add_item_inv('Сладкие трусики', 1, 9999)
    $ add_item_inv('Хлеб', 1, 25)
    
    $ shop_stock = {}
    $ add_item_shop('Вино', 10, 50)
    $ add_item_shop('Шоколад', 10, 20)
    $ add_item_shop('Банан', 10, 15)
    $ add_item_shop('Презервативы', 10, 75)
    
    $ events = []
    $ girls_points = {'Микки': {'лп': 0}, 'Кэйлин': {'лп': 0}, 'Одри': {'лп': 0}, 'Ирен': {'лп': 0}, 'Шеннон': {'лп': 0}}
    
    $ Fist = Weapon('Fist', 15)
    $ Alex = Player('Alexander', 120, 10, Fist)
    return
init python:
    coords = [[0], [0]]
    zone = 'zone1'
    def add_location(zone, location):
        global zone1
        global zone2
        global zone3
        global zone4
        global zone5
        if zone == 'zone1':
            zone1.append(location)
        elif zone == 'zone2':
            zone2.append(location)
        elif zone == 'zone3':
            zone3.append(location)
        elif zone == 'zone4':
            zone4.append(location)
        elif zone == 'zone5':
            zone5.append(location)
       
label start:
    #jump zone_0_pos_0_pos
    $ inventory = {}
    $ add_item_inv('Талеры', 50, 1)
    $ add_item_inv('Сладкие трусики', 1, 9999)
    $ add_item_inv('Хлеб', 1, 25)
    $ shop_stock = {}
    $ add_item_shop('Вино', 10, 50)
    $ add_item_shop('Шоколад', 10, 20)
    $ add_item_shop('Банан', 10, 15)
    $ add_item_shop('Презервативы', 10, 75)
    define me = Character("Alexander", who_color="#ffffff")
    define th = Character("Alexander's mind", who_color="#ffffff", who_prefix="~", who_suffix="~")
    define mky = Character("Mickey", who_color="#ff0000")
    define kln = Character("Keilin", who_color="#f7ff00")
    define aud = Character("Audrey", who_color="#1a00ff")
    define irn = Character("Iren", who_color="#02d9c7")
    $ kln_lp = 0
    $ meet_micky_and_imp_removed = False
    $ saved_micky = False
    $ micky_was_beaten = False
    $ keilin_with_alex = False
    $ zone1 = []
    $ zone2 = []
    $ zone3 = []
    $ zone4 = []
    $ zone5 = []
    menu:
        "Тестим словарь":
            jump test1
        "Тестим сейвы":
            call screen test_save
        "Тестим магаз":
            call screen shop
        "Тестим инвентарь":
            call screen inventory
    call screen shop
    jump zone_0_pos_0_pos
    jump prologue
    
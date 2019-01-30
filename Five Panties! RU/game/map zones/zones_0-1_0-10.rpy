label zone_0_pos_1_neg:
    if zone == 'zone1':
        if 'room1' not in zone1:
            #$ room1_scene = renpy.random.choice("#000", "#000") тут типа должен быть путь до изображений, но его нет хД
            scene room1_scene
            $ add_location('zone1', 'room1')
        else:
            scene room1_scene
        "Тут пусто."
        jump zone_0_pos_0_pos
    
label zone_0_pos_2_neg:
    "Тут пусто"
    jump zone_0_pos_0_pos
    
label zone_0_pos_3_neg:
    "Тут пусто"
    jump zone_0_pos_0_pos
    
label zone_0_pos_4_neg:
    "Тут пусто"
    jump zone_0_pos_0_pos
    
label zone_0_pos_5_neg:
    "Тут пусто"
    jump zone_0_pos_0_pos
 
label zone_0_pos_6_neg:
    "Тут пусто"
    jump zone_0_pos_0_pos
    
label zone_0_pos_7_neg:
    "Тут пусто"
    jump zone_0_pos_0_pos
    
label zone_0_pos_8_neg:
    "Тут пусто"
    jump zone_0_pos_0_pos
    
label zone_0_pos_9_neg:
    "Тут пусто"
    jump zone_0_pos_0_pos
    
label zone_0_pos_10_neg:
    "Тут пусто"
    jump zone_0_pos_0_pos
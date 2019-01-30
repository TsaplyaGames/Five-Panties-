init 3 python: 
    from datetime import datetime
    def get_time():
        global cur_hour, cur_time
        cur_hour = datetime.now().hour
        cur_time = datetime.now().time()
    Fist = Weapon('Fist', 15)
    Alex = Player('Alexander', 120, 10, Fist)
    cur_hour = datetime.now().hour
    cur_time = datetime.now().time()
    mp = MultiPersistent('fivepanties!')
    
    
init 4 python:
    
    import pickle
    
    test_dict = {'lol': 1, 'kek': 2}
    
    def test_save():
        global test_dict
        with open('test_dict.pickle', 'wb') as f:
            pickle.dump(test_dict, f)
            
    def test_load():
        global test_dict
        with open('test_dict.pickle', 'rb') as f:
            test_dict = pickle.load(f)
            
screen test_save:
    textbutton 'lol' xpos 0.5 ypos 0.5 action [Function(test_save), Hide('test_save'), Jump('test1')]
    
screen test_dict:
    vbox xpos 0.5 ypos 0.5:
        text str(test_dict['lol'])
        text str(test_dict['kek'])
        #textbutton 'up' action SetDict('test_dict', 'lol', 3)
        textbutton 'close' action [Hide('test_dict'), Jump('start')]
        
label test1:
    $ test_dict['lol'] += 2
    call screen test_dict
    
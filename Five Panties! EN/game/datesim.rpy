init 1 python:
    
    events = []
    
    girls_points = {'Микки': {}, 'Кэйлин': {}, 'Одри': {}, 'Ирен': {}, 'Шеннон': {}}
    
    def add_event(name):
        global events
        events.append(name)
        
    def del_event(name):
        global events
        events.remove(name)
        
    def add_point(girl, point, num):
        global girls_points
        girls_points[girl][point] += num
    
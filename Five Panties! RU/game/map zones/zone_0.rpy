label zone_0_pos_0_pos:
    menu:
        "Вверх":
            if coords[1][0] == 9:
                "Вы дошли до конца коридора, и стукнулись головой о стенку, минус 10 хп"
                jump zone_0_pos_0_pos
            else:
                $ coords[1][0] += 1
                "Вы продолжаете идти вверх [coords[0][0]] [coords[1][0]]"
                if coords[0][0] >= 0 and coords[1][0] >= 0:
                    $ renpy.jump('zone_' + str(coords[0][0]) + '_pos_' + str(coords[1][0]) + '_pos')
                elif coords[0][0] < 0 and coords[1][0] < 0:
                    $ renpy.jump('zone_' + str(coords[0][0])[1:] + '_neg_' + str(coords[1][0])[1:] + '_neg')
                elif coords[0][0] >= 0 and coords[1][0] < 0:
                    $ renpy.jump('zone_' + str(coords[0][0]) + '_pos_' + str(coords[1][0])[1:] + '_neg')
                elif coords[0][0] < 0 and coords[1][0] >= 0:
                    $ renpy.jump('zone_' + str(coords[0][0])[1:] + '_neg_' + str(coords[1][0]) + '_pos')
        "Влево":
            if coords[0][0] == 9:
                "Из-за леса, из-за гор прилетел в ебло топор. Минус 20 хп"
                jump zone_0_pos_0_pos
            else:
                $ coords[0][0] += 1
                "Вы продолжаете идти влево [coords[0][0]] [coords[1][0]]"
                if coords[0][0] >= 0 and coords[1][0] >= 0:
                    $ renpy.jump('zone_' + str(coords[0][0]) + '_pos_' + str(coords[1][0]) + '_pos')
                elif coords[0][0] < 0 and coords[1][0] < 0:
                    $ renpy.jump('zone_' + str(coords[0][0])[1:] + '_neg_' + str(coords[1][0])[1:] + '_neg')
                elif coords[0][0] >= 0 and coords[1][0] < 0:
                    $ renpy.jump('zone_' + str(coords[0][0]) + '_pos_' + str(coords[1][0])[1:] + '_neg')
                elif coords[0][0] < 0 and coords[1][0] >= 0:
                    $ renpy.jump('zone_' + str(coords[0][0])[1:] + '_neg_' + str(coords[1][0]) + '_pos')
        "Вправо":
            if coords[0][0] == -10:
                "К вам сзади пристроился Тёмный Властелин, минус 30 хп и потеря анальной девственности"
                jump zone_0_pos_0_pos
            else:
                $ coords[0][0] -= 1
                "Вы продолжаете идти вправо [coords[0][0]] [coords[1][0]]"
                if coords[0][0] >= 0 and coords[1][0] >= 0:
                    $ renpy.jump('zone_' + str(coords[0][0]) + '_pos_' + str(coords[1][0]) + '_pos')
                elif coords[0][0] < 0 and coords[1][0] < 0:
                    $ renpy.jump('zone_' + str(coords[0][0])[1:] + '_neg_' + str(coords[1][0])[1:] + '_neg')
                elif coords[0][0] >= 0 and coords[1][0] < 0:
                    $ renpy.jump('zone_' + str(coords[0][0]) + '_pos_' + str(coords[1][0])[1:] + '_neg')
                elif coords[0][0] < 0 and coords[1][0] >= 0:
                    $ renpy.jump('zone_' + str(coords[0][0])[1:] + '_neg_' + str(coords[1][0]) + '_pos')
        "Вниз":
            if coords[1][0] == -10:
                "Вы зашли в тупиковую ветку и споткнувшись, упали в проломленный пол, минус 10 хп"
                jump zone_0_pos_0_pos
            else:
                $ coords[1][0] -= 1
                "Вы продолжаете идти вниз [coords[0][0]] [coords[1][0]]"
                if coords[0][0] >= 0 and coords[1][0] >= 0:
                    $ renpy.jump('zone_' + str(coords[0][0]) + '_pos_' + str(coords[1][0]) + '_pos')
                elif coords[0][0] < 0 and coords[1][0] < 0:
                    $ renpy.jump('zone_' + str(coords[0][0])[1:] + '_neg_' + str(coords[1][0])[1:] + '_neg')
                elif coords[0][0] >= 0 and coords[1][0] < 0:
                    $ renpy.jump('zone_' + str(coords[0][0]) + '_pos_' + str(coords[1][0])[1:] + '_neg')
                elif coords[0][0] < 0 and coords[1][0] >= 0:
                    $ renpy.jump('zone_' + str(coords[0][0])[1:] + '_neg_' + str(coords[1][0]) + '_pos')
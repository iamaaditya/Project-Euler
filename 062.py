def cube_permuations():
    i = 1
    cube_dic = {}
    while True:
        #if not i % 10 : continue
        i3 = i**3
        i3s = ''.join(sorted(str(i3)))
        #print type(i3s), ''.join(i3s)
        if i3s in cube_dic:
            cube_dic[i3s].append(i3)
            if len(cube_dic[i3s]) >= 5:
                print sorted(cube_dic[i3s])
                return
        else:
            cube_dic[i3s] = [i3]
        i += 1

cube_permuations()

        


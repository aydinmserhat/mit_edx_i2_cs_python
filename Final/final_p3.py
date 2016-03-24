# d = {8: 6, 2: 6, 4: 6, 6: 6}
d = {1:10, 2:20, 3:30, 4:30}
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    dic = {}
    for key in d:
        if d.get(key) not in dic:
            dic[d.get(key)] = [key]

        elif d.get(key) in dic:
            dic[d.get(key)] = sorted(dic[d.get(key)] + [key])

    return dic

print dict_invert(d)

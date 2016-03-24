def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    intersect = {}
    diff = {}

    for key1 in d1.keys():
        if key1 in d2.keys():
            a = d1.get(key1,0)
            b = d2.get(key1,0)
            intersect[key1] = f(a, b)
        if key1 not in d2.keys():
            val1 = d1[key1]
            diff[key1] = val1

    for key2 in d2.keys():
        if key2 not in d1.keys():
            val2 = d2[key2]
            diff[key2] = val2
    t = (intersect, diff)
    return t

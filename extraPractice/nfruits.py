def nfruits(fruits, pattern):
    assert len(fruits) <= 10, "it should not bigger than 10"
    assert len(fruits) != 0, "it should not equal to 0"

    for char in pattern[:-1]:
        v = fruits
        fruits = { k:(v+1) for k, v in v.items() if k != char }
        fruits[char] = v[char] - 1
            
    fruits[pattern[-1]] = fruits[pattern[-1]] - 1
    return fruits[max(fruits, key=lambda x:fruits[x])]


print nfruits({'Y': 5, 'D': 9, 'O': 7, 'V': 7}, 'D')
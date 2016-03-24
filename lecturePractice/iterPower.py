def iterPower(base, exp):
    result = 1
    while exp > 0:
        result = result * base
        exp = exp - 1
    return result    
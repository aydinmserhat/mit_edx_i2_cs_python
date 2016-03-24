def recurPower(base, exp):
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return base*recurPower(base,exp-1)
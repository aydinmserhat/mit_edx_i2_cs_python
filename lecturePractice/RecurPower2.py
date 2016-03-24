def recurPowerNew(base, exp):
    if exp > 0 and exp % 2 == 0:
        return recurPowerNew(base,exp/2.0)*recurPowerNew(base,exp/2.0)
    elif exp > 0 and exp % 2 == 1:
        return base*recurPowerNew(base,exp-1)
    elif exp == 0:
        return 1


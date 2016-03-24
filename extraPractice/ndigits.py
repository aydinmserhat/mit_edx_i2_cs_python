def ndigits(x):
    if 0 <= x < 10: # for single, digit return 1
        return 1
    elif x < 0:
        return 1 + ndigits(-x/10) # put minus sign into the recursive function, for negative numbers 
    else:
        return 1 + ndigits(x/10) #  for positive numbers 
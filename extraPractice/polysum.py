import math
def polysum(n,s):
    area = (0.25*n*s**2)/(math.tan(math.pi/n))
    perimeter = n*s
    sq_per = perimeter**2
    sum = area + sq_per
    sum = round(sum,4)
    return sum
    
def item_order(order):
    numSalad = order.count("salad")
    numHamburger = order.count("hamburger")
    numWater = order.count("water")
    return "salad:{} hamburger:{} water:{}".format(numSalad, numHamburger, numWater)
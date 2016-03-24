def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    handLen = 0
    for val in hand.values():
        handLen = handLen + val
    return handLen
    ## return sum(hand.values())  "gives same result"

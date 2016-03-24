def biggest(aDict):
    result = None
    biggestValue = 0
    for key in aDict.keys():

        if len(aDict[key]) >= biggestValue:
            biggestValue = len(aDict[key])
            result = key

    return result

    # This time, write a procedure, called biggest,
    # .. which returns the key corresponding to the entry with the largest number of values associated with it.
    # .. If there is more than one such entry, return any one of the matching keys.

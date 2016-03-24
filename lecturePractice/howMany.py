def howMany(aDict):
    sum = 0
    for value in aDict.values():
        sum = sum + len(value)
    return sum

    # animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
    # We want to write some simple procedures that work on dictionaries to return information.

    # First, write a procedure, called howMany, which returns the sum of the number of values associated with a dictionary.

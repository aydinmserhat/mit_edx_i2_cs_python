def oddTuples(aTup):
    result = ()
    for index in range(len(aTup)):
        if index % 2 == 0:
            result = result + (aTup[index],)
    return result


    # Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output,

    #.. where every other element of the input tuple is copied, starting with the first one.

    #.. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return

    #.. the tuple ('I', 'a', 'tuple').

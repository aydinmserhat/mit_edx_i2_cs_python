def isPalindrome(aString):
    if len(aString) == 1:  # for odd number of letters of aString
        return True
    if len(aString) == 0:  # for even number of letters of aString
        return True
    if aString[0] == aString[-1]:
        return isPalindrome(aString[1:-1])
    elif aString[0] != aString[-1]:
        return False

    
    # Write a Python function that returns True if aString is a palindrome (reads the same forwards or reversed) and False otherwise.
    # Do not use Python's built-in reverse function or aString[::-1] to reverse strings.

    # This function takes in a string and returns a boolean.


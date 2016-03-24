print("Please think of a number between 0 and 100!")
hi = 100
lo = 0

while True:
    guess = (hi+lo)/2
    print("Is your secret number " + str(guess)+ "?")
    #inp = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    inp = raw_input("enter: ")
    if inp == "h":
        hi = guess
    elif inp == "l":
        lo = guess
    elif inp == "c":
        break
    else:
        print("Sorry, I did not understand your input.")
print('Game over. Your secret number was: ' + str(guess))
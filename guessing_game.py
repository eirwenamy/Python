secret_word = "Rossum"
guess = ""
guessCount = 0
guessLimit = 3
outofguesses = False

while guess != secret_word and not(outofguesses):
    if guessCount < guessLimit:
        guess = input("Enter guess: ")
        guessCount+=1
    else:
        outofguesses = True
if outofguesses:
    print('you are out of guesses. you lose!')
else:
    print('you won!')
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lsw = len(secretWord)
    lettersGuessed = list()
    #mistakeMade = list()
    print('Welcome to the game Hangman!')    
    print('I am thinking of a word that is ' + str(lsw) + ' letters long')
    #print('-----------')
    i = 8    
    while i > 0:
        print('-----------')
        print('You have ' + str(i) + ' guesses left' )
        print('Available letters: ' + 
                str(getAvailableLetters(lettersGuessed)))
        guess = input('Please guess a letter: ')
        guessInLowerCase = guess.lower()
        
        
        if guessInLowerCase not in getAvailableLetters(lettersGuessed):
            print("Oops! You've already guessed that letter: " +
            str(getGuessedWord(secretWord, lettersGuessed)))
            
        

        elif (guessInLowerCase not in secretWord)== True:
            lettersGuessed.append(guessInLowerCase)            
            i -= 1
            print('Oops! That letter is not in my word: ' +
            str(getGuessedWord(secretWord, lettersGuessed)))
            if i==0:
                print('-----------')
                print('Sorry, you ran out of guesses. The word was '+
                str(secretWord) + '.')

        
        elif (guessInLowerCase in secretWord) == True:
            lettersGuessed.append(guessInLowerCase)            
            print('Good guess: ' + 
            str(getGuessedWord(secretWord, lettersGuessed)))
            
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print('-----------')
                print('Congratulations, you won!')
                break

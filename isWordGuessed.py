def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    bol = list() 
    for i in range(len(secretWord)):
        for j in range(len(lettersGuessed)):
            bol_True = secretWord[i]==lettersGuessed[j]
            if bol_True == True:
                bol.append(secretWord[i]==lettersGuessed[j])
    if len(bol) >= len(secretWord):
        return True
    else:
        return False

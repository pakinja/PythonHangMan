def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    #bol = list()
    pos = list()
    dicc = dict()
    
    if len(lettersGuessed)== 0:
        for k in range(len(secretWord)):  
            dicc[k] = ' _ '
    else:
            
        for i in range(len(secretWord)):
            for j in range(len(lettersGuessed)):
                
                bol_True = secretWord[i]==lettersGuessed[j]
                if bol_True == True:
                    dicc[i] = secretWord[i]
                    pos.append(i)
                    break
                elif bol_True == False:
                    dicc[i] = ' _ '
    val_string = ''.join(dicc.values())
    return val_string

# Function for token creation
def tokenization(fileName):
    f = open(fileName, 'r')
    
    ##  Sample input sentence
    ##  Habo\PREP siyang\PRON magiba\VB sa\CONJ agom\NN niya\PRON sa\CONJ plataporma\NN sa\CONJ pagkakampya\VB .\PUNCT

    ## Example output for incomplete tags
    ## [('Laman', 'None'), ('kaini', 'None'), ('an', 'DET'), ('apatnapulong', 'None')
    ## ,('(40)', 'None'), ('rawitdawit', 'None'), ('.', 'PUNCT,')]

    ## Example output for complete tags
    ## [('Habo', 'PREP'), ('siyang', 'PRON'), ('magiba', 'VB'), ('sa', 'CONJ'),
    ## ('agom', 'NN'), ('niya', 'PRON'), ('sa', 'CONJ'),
    ## ('plataporma', 'NN'), ('sa', 'CONJ'), ('pagkakampya', 'VB'), ('.', 'PUNCT')]

    sentences = f.read().splitlines()
    listSentences = []
    tokenizedWords = []
    tokenizedSentence = []

    ##  Inserting all sentences into an array  
    for idx, sentence in enumerate(sentences):
        splittedSentence = sentences[idx].split()
        listSentences.insert(idx, splittedSentence)

    # print(len(listSentences))

    tokens = 0

    ##  For separating the words and their tags 
    for sentence in listSentences:
        for word in sentence:
            tempWord = word.split('\\')
            tokenizedPair = tuple(tempWord)
            tokenWord = tokenizedPair[0]
            tokens+=1

            if len(tokenizedPair) == 1:
                tokenizedPair = list(tokenizedPair)
                tokenizedPair.append('None')
                tokenizedPair = tuple(tokenizedPair)
            else:
                tokenTag = tokenizedPair[1]

            ## Inserting tokenized pairs into an array
            tokenizedWords.append(tokenizedPair)
            
            ## Final output would be an array of sentences with their tags
            if tokenWord == '.':
                tokenizedSentence.append(tokenizedWords)
                tokenizedWords = []

    f.close()
    return tokenizedSentence
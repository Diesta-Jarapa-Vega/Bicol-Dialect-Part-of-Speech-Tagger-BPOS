import warnings
import string, re
from collections import Counter

## Function to find most frequent words
def frequency(file, Counter):
    f = open(file, 'r')
    sentences = f.read().splitlines()
    listSentences = []
    tokenWords = []
  
    for idx, sentence in enumerate(sentences):
        splittedSentence = sentences[idx].split()
        listSentences.insert(idx, splittedSentence)

    for sentence in listSentences:
        for word in sentence:
            tempWord = word.split('\\')
            tokenizedPair = tuple(tempWord)
            tokenWord = tokenizedPair[0]
            tokenWords.append(tokenWord)

    Counter = Counter(tokenWords)
    frequent = Counter.most_common(20)
    
    f.close()
    return frequent

tokens = frequency('bpostagger/datasets/tagged.txt', Counter)

frequentwords = []
for token in tokens:
    token = token[0]
    frequentwords.append(token)

## Main Feature Functions
def features(sentence, index, frequentwords):

    return { 
        'word': sentence[index],
        'is_firstword': index == 0,
        'is_lastword': index == len(sentence) - 1,
        'is_mostfrequentword': sentence[index] in frequentwords, 
        'is_firstcapital': sentence[index][0].upper() == sentence[index][0],
        'is_all_caps': sentence[index].upper() == sentence[index],
        'is_all_lower': sentence[index].lower() == sentence[index],
        'prefix-1': sentence[index][0],
        'prefix-2': sentence[index][:2],
        'prefix-3': sentence[index][:3],
        'suffix-1': sentence[index][-1],
        'suffix-2': sentence[index][-2:],
        'suffix-3': sentence[index][-3:],
        'is_long': len(sentence[index]) > 3,
        'is_short': len(sentence[index]) <= 3,
        'prev_word': '' if index == 0 else sentence[index - 1],
        'next_word': '' if index == len(sentence) - 1 else sentence[index + 1],
        'has_hyphen': '-' in sentence[index],
        'capitals_inside': sentence[index][1:].lower() != sentence[index][1:],
        'is_NUM': sentence[index].isdigit(),
        'is_PUNCT': sentence[index] in string.punctuation,
        'has_VB_prefix_1': sentence[index][:3] == 'mag' or sentence[index][:3] == 'Mag',
        'has_VB_prefix_2': sentence[index][:4] == 'nag-' or sentence[index][:4] == 'Nag-',
        'has_VB_prefix_3': sentence[index][:4] == 'maka' or sentence[index][:4] == 'Maka',
        'has_VB_prefix_4': sentence[index][:4] == 'naka' or sentence[index][:4] == 'Naka',
        'has_VB_prefix_5': sentence[index][:5] == 'makaka' or sentence[index][:5] == 'Makaka',
        'has_VB_prefix_6': (sentence[index][:4] == 'mapa' or sentence[index][:4] == 'Mapa') and len(sentence[index]) > 3 ,
        'has_NN/ADV_prefix_1': (sentence[index][:3] == 'pag' or sentence[index][:3] == 'Pag') and len(sentence[index]) > 3,
        'has_NN_prefix_2': (sentence[index][:4] == 'pang' or sentence[index][:4] == 'Pang') and len(sentence[index]) > 4,
        'has_NN/ADV_prefix_3': (sentence[index][:5] == 'pagka' or sentence[index][:5] == 'Pagka') and len(sentence[index]) > 5,
        'NN_prev_word': len(sentence[index-1]) == 3 or len(sentence[index-1]) == 2,
        'ADJ_prev_word': sentence[index - 1] == 'mas' or sentence[index - 1] == 'Mas',
        'has_ADJ_suffix_1': sentence[index][-3:] =='ong' or sentence[index][-2:] =='on',
        'has_ADJ_prefix_1': sentence[index][:6] == 'pinaka' or sentence[index][:6] == 'Pinaka',
        'has_ADJ_prefix_2': sentence[index][:2] == 'ma' or sentence[index][:2] == 'Ma',
        'has_ADJ_prefix_4': sentence[index][0].upper() == sentence[index][0] and sentence[index][-3:] =='ong',
    }
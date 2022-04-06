from asyncore import loop
from json import JSONDecoder
from functools import partial

def json_parse(fileobj, decoder=JSONDecoder(), buffersize=5000):
    buffer = ''
    for chunk in iter(partial(fileobj.read, buffersize), ''):
        buffer += chunk
        while buffer:
            try:
                result, index = decoder.raw_decode(buffer)
                yield result
                buffer = buffer[index:].lstrip()
            except ValueError:
                # Not enough data to decode, read more
                break


def findWord(word):
    tempPosTags = []
    with open('Bicol-Words-Dictionary.json', 'r') as infh:
        for data in json_parse(infh):
            if word == data['word']:
                tempPosTags.append('/' + data['pos'])
    posTag = ''.join(tempPosTags)
    if tempPosTags:
        return posTag


with open('dataset_10.txt', encoding="utf8") as f:
    datasets = []
    for line in f.readlines():
        sentence = []
        for word in line.split():
            
            word = str(word)
            res = word[0].lower() + word[1:]
            posTag = findWord(res)
            if posTag == None:
                wordPos = word
            else:
                wordPos = word + posTag
            sentence.append(wordPos)
        combined = ' '.join(sentence)
        datasets.append(combined)
        print(combined)
    with open('tagged_dataset_10.txt', 'w', encoding='utf-8') as f:
        for line in datasets:
            f.write(line)
            f.write('\n')


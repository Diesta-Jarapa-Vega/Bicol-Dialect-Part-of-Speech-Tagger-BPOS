# code to check words with no tags yet
import sys, os
basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

#f = open('C:/Users/Rica/Desktop/BPOS/datasets/tagged-2.txt', 'r')
f = open(os.path.join(basedir, "datasets", "tagged_validated.txt"), 'r')

sentences = f.read().splitlines()
listSentences = []

for idx, sentence in enumerate(sentences):
    splittedSentence = sentences[idx].split()
    listSentences.insert(idx, splittedSentence)

wordcount = 0
count = 0
c = 0

for sentence in listSentences:
    for word in sentence:
      wordcount+=1
      if "\\" not in word:
        count+=1
        print(word)

# to find non-ascii characters
for sentence in listSentences:
  for word in sentence:
    for letter in word:
      ascii = letter.isascii()
      if ascii == False:
        print(letter)
        if letter in word:
          print(word)

print("\ntotal words: ", wordcount)
print("number of words untagged: ", count)
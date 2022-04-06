import time
from unicodedata import digit
import nltk
import scipy.stats
import string, re
import matplotlib.pyplot as plt
from itertools import chain
from collections import Counter
from nltk.tag.util import untag
from sklearn_crfsuite import CRF, metrics
from tokenizer import tokenization
from features import features
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import classification_report

tagged_sentences = tokenization('bpostagger/datasets/tagged.txt')

cutoff = int(.80 * len(tagged_sentences))
training_sentences = tagged_sentences[:cutoff]
test_sentences = tagged_sentences[cutoff:]

def transform_to_dataset(tagged_sentences):
    X, y = [], []
 
    for tagged in tagged_sentences:
        X.append([features(untag(tagged), index, frequentwords='') for index in range(len(tagged))])
        y.append([tag for _, tag in tagged])
 
    return X, y
 
X_train, y_train = transform_to_dataset(training_sentences)
traincount = 0
for sent in X_train:
    for word in sent:
      traincount+=1

X_test, y_test = transform_to_dataset(test_sentences)
testcount = 0
for sent in X_test:
    for word in sent:
      testcount+=1
 
print("Sentences in trainset:", len(X_train))
print("Tokens in trainset:", traincount)     
print("Sentences in testset:", len(X_test))
print("Tokens in trainset:", testcount)

## Display train and test values
# print(y_test[0])
# print(X_test) # dict
# print(X_train) # dict
# print(y_train[0])

# CRF fitting
model = CRF(
  algorithm ='lbfgs',
    c1 = 0.01,
    c2 = 0.1,
    max_iterations = 100,
    all_possible_transitions = True
)
model.fit(X_train, y_train)  

## POS tag list
labels = list(model.classes_)

## Getting Predicted Values from trained set
y_pred = model.predict(X_train)

## F1 score and accuracy score on train dataset
print("\nFor Training Set: ")
print("F1 score:          {}".format(metrics.flat_f1_score(y_train, y_pred, average='weighted')))
print("Precision score:   {}".format(metrics.flat_precision_score(y_train, y_pred, average='weighted')))
print("Recall score:      {}".format(metrics.flat_recall_score(y_train, y_pred, average='weighted', labels=labels)))

y_pred = model.predict(X_test)

## F1 score and accuracy score on test dataset
print('\n')
print("For Testing Set: ")
print("F1 score:          {}".format(metrics.flat_f1_score(y_test, y_pred, average='weighted')))
print("Precision score:   {}".format(metrics.flat_precision_score(y_test, y_pred, average='weighted')))
print("Recall score:      {}".format(metrics.flat_recall_score(y_test, y_pred, average='weighted', labels=labels)))


## Transform multi-label data to binary array for classification report
mlb = MultiLabelBinarizer()
y_pred = mlb.fit_transform(y_pred)
y_test = mlb.fit_transform(y_test)

## Classification Report
report = classification_report(y_test, y_pred, labels=None, target_names=labels,        
    sample_weight=None,
    digits=3,
    output_dict=False,
    zero_division="warn") 
print("\n")
print(report)
    

## Transition Features
print("\nTRANSITION FEATURES: ", len(model.transition_features_))

def transitionfeatures(transition_features):
    for (label_from, label_to), weight in transition_features:
        print("%-6s-->%-7s %0.6f" % (label_from, label_to, weight))

print("\nMost Likely Transition Features: \n")
transitionfeatures(Counter(model.transition_features_).most_common(20))

print("\nUnlikely Transitions Features: \n")
transitionfeatures(Counter(model.transition_features_).most_common()[-20:])

## State Features
print("\nSTATE FEATURES : ", len(model.state_features_))

def statefeatures(state_features):
    for (label_from, label_to), weight in state_features:
        print("%-25s-->%-7s %0.6f" % (label_from, label_to, weight))

print('\nMost Likely State Features:\n')
statefeatures(Counter(model.state_features_).most_common(20))

print('\nUnlikely State Features:\n')
statefeatures(Counter(model.state_features_).most_common()[-20:])

## Function that checks for special characters
def check_special_char(word):

    if re.search(r"\,",word):
        return True
    elif re.search(r"\.",word):
        return True
    else:
        return False

## Function for processing user sentence input
def getUserInput(userInput):
    user_input = userInput.split(" ")
    updated_input = []
    for word in user_input:
        if check_special_char(word) == False:
            updated_input.append(word)
        else:
            for letter in word:
                if letter in string.punctuation:
                    new_word = word.replace(letter, '')
                    updated_input.append(new_word)
                    updated_input.append(letter)
    return updated_input


## Function for POS Tagger
def pos_tag(sentence):
    sentence_features = [features(sentence, index, frequentwords='') for index in range(len(sentence))]
    taggedSentence = list(zip(sentence, model.predict([sentence_features])[0]))
    finalSet = []
    for i in range(0, len(taggedSentence) - 1):
        finalSet.append(taggedSentence[i])
        finalSet.append(tuple([' ', 'None']))
    finalSet.append(taggedSentence[-1])
    print(finalSet)
    return finalSet
import json
from classifiers import *
from nltk.probability import FreqDist

classifiers = [getClassifier(objsa2), getClassifier(objsa3), getClassifier(objsa4), getClassifier(objsa6), getClassifier(objsa7), getClassifier(
    objsa8), getClassifier(objsa9), getClassifier(objsb1), getClassifier(objsb4), getClassifier(objsb6), getClassifier(objsc1)]

# Aquí se reciben los json con los posts a evaluar
tests = open('tests/tests.json', 'r', encoding='utf8')
testsText = tests.read()
testsObj = json.loads(testsText)

testsObj = getTokenizedText(testsObj)
total_words = []

results = []
for test in testsObj:
    test['text'] = removeWords(test['text'])
    total_words += test['text']
    [stemmed] = stemming([test])
    test = stemmed
    postTags = []
    for classifier in classifiers:
        test_document = documentFeatures(test, classifier[1])
        postTags.append(classifier[0].classify(test_document))

    results.append([test, postTags])

for result in results:
    print(result)

all_words = FreqDist(total_words)
words_used = list(all_words.keys())[:10]
print(words_used)

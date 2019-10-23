from nltk.corpus import movie_reviews
from nltk.probability import FreqDist
import nltk
import random


documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)


all_words = FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words.keys())[:2000]
for w in word_features:
    print(w)


"""def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


featuresets = [(document_features(d), c) for (d, c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(len(train_set))
print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

stop_words = set(stopwords.words('spanish'))

text = 'Hola, me llamo Gabriel, esto es una prueba para usar nltk, así que lo estoy usando, también uso mis juguetes'
tokenized_word = word_tokenize(text)
print(tokenized_word)


# Quitamos palabras que hacen ruido
filtered_sent=[]
for w in tokenized_word:
    if w not in stop_words:
        filtered_sent.append(w)

print('Filtered sentence:',filtered_sent)


# Stemming
stemmer = SnowballStemmer('spanish')

stemmed_words=[]
for w in filtered_sent:
    stemmed_words.append(stemmer.stem(w))

print('Stemmed sentence:',stemmed_words)
"""
lem = WordNetLemmatizer()

word="flying"
print('Lemmatized word: ', lem.lemmatize(word,'v'))
"""
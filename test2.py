import nltk
nltk.download('words')
words = set(nltk.corpus.words.words())
print(words)
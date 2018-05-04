
from textblob import TextBlob

text = '''
The Earth is a very small stage in a vast cosmic arena. 

I got the worse grades this semester.

They lived happily ever after.

i feel feverish and cold after it rains.
'''

blob = TextBlob(text)

print(blob.tags)           # [('The', 'DT'), ('titular', 'JJ'),
print("")                    #  ('threat', 'NN'), ('of', 'IN'), ...]

print(blob.noun_phrases)   # WordList(['titular threat', 'blob',
print("")                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])

for sentence in blob.sentences:
    print(sentence)
    #analysis = TextBlob(sentence)
    print(sentence.sentiment)
    print("")
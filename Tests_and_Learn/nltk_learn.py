import nltk
# nltk.downloader.download('all')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pickle

# example_text = "I cant praise your courses enough. Not only do they offer an introduction, but you seem to be able to seamlessly progress and transition into the really useful complex tools too. Not only this course, but all of them. I use Udemy and Datacamp a lot, and they are both excellent, but your python courses really are a step above even DataCamp. Thank you so much  !!!"

with open('data\comment_black_adam_review_text.pickle','rb') as input_file:
    reloaded_copy_of_texts = pickle.load(input_file)

reloaded_copy_of_texts = str(reloaded_copy_of_texts)

print(word_tokenize(reloaded_copy_of_texts))

# for i in word_tokenize(example_text):
#     print(i)

stop_words = set(stopwords.words("english"))
# print (stop_words)

words = word_tokenize(reloaded_copy_of_texts)

filtered_sentence = []

for w in words: 
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)



# # stemming
# ps = PorterStemmer()
# # example_words = ("python","pythoner","pythonic","pythoning","pythonly",)
# # for st in example_words:
# #     print(ps.stem(st))

# for st in filtered_sentence:
#     print(ps.stem(st))



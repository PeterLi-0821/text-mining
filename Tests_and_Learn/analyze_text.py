#requirement
import praw
import pickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.downloader.download('vader_lexicon')
from string import *
from random import *

# Load data from a file (will be part of your data processing script)
with open('data\comment_text.pickle','rb') as input_file:
    reloaded_copy_of_texts = pickle.load(input_file)

# print(reloaded_copy_of_texts)



def count_words(comments):                  
    skips = [".", ", ", ":", ";", "'", '"'] 
    for ch in skips: 
        for comment in comments:
          comment = comment.replace(ch, "") 
    
    word_counts = {} 
    
    for comment in comments:
      for word in comment.split(" "): 
          if word in word_counts: 
              word_counts[word]+= 1 
          else: 
              word_counts[word]= 1 
    res = sorted(word_counts.items(), key=lambda item: item[1])
    res.reverse()
    return res
    
print(count_words(reloaded_copy_of_texts))

def sentiment(text):
    scores = []
    for comment in (text):
        score = SentimentIntensityAnalyzer().polarity_scores(comment)
        scores.append(score['compound'])
        return score['compound']

    avg = sum(scores)/len(scores)
    return avg
    
# https://stackoverflow.com/questions/43546593/error-message-with-nltk-sentiment-vader-in-python
# nltk.downloader.download('vader_lexicon')
# comment = 'Very disappointing. I was looking forward to another powerful and nuanced performance from The Rock.'
# score = SentimentIntensityAnalyzer().polarity_scores(comment)
# print(score)

print(sentiment(reloaded_copy_of_texts))

#requirement
import pickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.downloader.download('vader_lexicon')



with open('data\comment_black_adam_review_text.pickle','rb') as input_file:
    reloaded_copy_of_texts = pickle.load(input_file)


scores = []
for comment in reloaded_copy_of_texts:
  
  score = SentimentIntensityAnalyzer().polarity_scores(comment)
  scores.append(score['compound'])
  print(score['compound'])

avg = sum(scores)/len(scores)
print(avg)
nltk.downloader.download('vader_lexicon')
# comment = 'Very disappointing. I was looking forward to another powerful and nuanced performance from The Rock.'
# score = SentimentIntensityAnalyzer().polarity_scores(comment)
# print(score)


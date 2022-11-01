

import praw
import pandas

import matplotlib.pyplot as plt

reddit = praw.Reddit(client_id='Njsa5nEIEZo_fw1eZ6Jeaw', client_secret='s_ay0DlEShsU98VYMrr05Mlfobtttg', user_agent='test', username='peter09231023', password= 'Babson0821')

subreddit = reddit.subreddit ('wallstreetbets')

top_subreddit = subreddit.new (limit= 50)

count = 0
max = 10000
words = []
wordCount = {}
commonWords = {'that','this','THE','and','of','the','for','I','it','has','in',
'you','to','was','but','have','they','a','is','','be','on','are','an','or',
'at','as','do','if','your','not','can','my','their','them','they','with',
'at','about','would','like','there','You','from','get','just','more','so',
'me','more','out','up','some','will','how','one','what',"don't",'should',
'could','did','no','know','were','did',"it's",'This','he','The','we',
'all','when','had','see','his','him','who','by','her','she','our','thing','-',
'now','what','going','been','we',"I'm",'than','any','because','We','even',
'said','only','want','other','into','He','what','i','That','thought',
'think',"that's",'Is','much'}

for submission in subreddit.top(limit=5):
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        # count += 1
        # if(count == max):
        #     break
        word = ""
        for letter in top_level_comment.body:
            if(letter == ' '):
                if(word and not word[-1].isalnum()):
                    word = word[:-1]
                if not word in commonWords:
                    words.append(word)
                word = ""
            else:
                word += letter
    # if(count == max):
    #         break

for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

sortedList = sorted(wordCount, key = wordCount.get, reverse = True)
print(sortedList)


def count_words(text):                  

    word_counts = {} 
    for word in str((text)).split(" "): 
        if word in word_counts: 
            word_counts[word]+= 1 
        else: 
            word_counts[word]= 1 
    return word_counts 
  
    # >>>count_words(text) You can check the function 
print(count_words(sortedList))
# keyWords = []
# keyCount = []
# amount = 0

# for entry in sortedList:
#     keyWords.append(entry)
#     keyCount.append(wordCount[entry])
#     amount += 1
#     if (amount == 10):
#         break

# labels = keyWords
# sizes = keyCount
# # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

# plt.title('Top comments for: r/' + 'wallstreetbets')
# plt.pie(sizes, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# plt.show()
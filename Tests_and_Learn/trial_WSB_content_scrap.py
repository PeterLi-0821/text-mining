import praw
import string
import pickle
import base64

reddit = praw.Reddit(client_id='Njsa5nEIEZo_fw1eZ6Jeaw', client_secret='s_ay0DlEShsU98VYMrr05Mlfobtttg', user_agent='test', username='peter09231023', password= 'Babson0821')

#1. read reddit link to txt file

submission = reddit.submission(url="https://www.reddit.com/r/wallstreetbets/comments/yin4pn/what_are_your_moves_tomorrow_november_01_2022/")

submission.comments.replace_more(limit= None)
print('success')
comments_all = []
for comments in submission.comments:
    comment_body = comments.body
    comments_all.append(comment_body)
    # print(comments_all)

print(comments_all)
with open('comments_all','w') as f:
    pickle.dump(comments_all,f.decode('utf-8')) #TypeError: write() argument must be str, not bytes

def count_words(text):                  

    word_counts = {} 
    for word in str((text)).split(" "): 
        if word in word_counts: 
            word_counts[word]+= 1 
        else: 
            word_counts[word]= 1 
    return word_counts 


print(count_words(comments_all))
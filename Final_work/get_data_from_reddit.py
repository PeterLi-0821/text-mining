import praw
import pickle


reddit = praw.Reddit(client_id='Njsa5nEIEZo_fw1eZ6Jeaw', client_secret='s_ay0DlEShsU98VYMrr05Mlfobtttg', user_agent='test', username='peter09231023', password= 'Babson0821')

#1. read reddit link to a file

# submission = reddit.submission(url="https://www.reddit.com/r/entertainment/comments/y7jnts/black_adam_review_dwayne_johnsons_superhero_debut/")
submission = reddit.submission(url="https://www.reddit.com/r/wallstreetbets/comments/xdb7ex/this_is_the_us_stock_market/")


submission.comments.replace_more(limit=None)

comments_all = []
for comments in submission.comments:
    comment_body = comments.body
    comments_all.append(comment_body)

print(comments_all)


for comment in comments_all:
  print(comment)

# with open('comment_black_adam_review_text.pickle','wb') as f: #TypeError: write() argument must be str, not bytes, so changed w to wb
#     pickle.dump(comments_all,f) 

with open('comment_us_stock_market_text.pickle','wb') as f: 
    pickle.dump(comments_all,f) 

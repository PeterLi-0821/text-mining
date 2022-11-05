# Part 3: Project Writeup and Reflection

## 1. Project Overview

The source I use is Reddit. I found two links to Reddit posts with their sub-comments. I exported the contents extracted by the two links using praw and used pickle to create separate data files for both links. I first analyze the document by counting the total number of words and counted the most frequently appeared words to understand the data better. Then I used NLTK to know if the content is positive or negative. I hope to create a program to quickly understand the opinion on a certain topic from Reddit users because it is hard to read all the comments from different users with different opinions. 

## 2. Implementation、

The first python file is used for getting data from Reddit and converting the data into a file and storing it. Every time I try to use PRAW to get data from Reddit, it took a while to do so. Therefore, storing data is important and saves lots of time. In analyze text part, I first open the data file, then use the common code practiced in previous works to get word counts and excluded the stopwords. This is for understanding the text for further analysis. The new experience is using NLTK to get a score of the comments. The result of the sentiment analysis is a dictionary contains 4 keys and the only key I need is the compound. So I wrote a for loop to get compound scores for all the strings. Then I could get an average score for the overall post. 

## 3. Results

The main result is the positive or negative judgment concluded from comments read from Reddit. Using sentiment Vader I could get a score for all the comments. So I could tell people's opinions towards the movie *Black Adam* and *US Stock Market*, Which both have slightly positive comments. However, what I found that may harm the accuracy of nltk analysis is that there are special terms for the stock market and normal English may not fit in this situation. The further study would be developing special codes only for the use of analyzing the stock market.

Links: 
- [Black Adam](https://www.reddit.com/r/entertainment/comments/y7jnts/black_adam_review_dwayne_johnsons_superhero_debut/)
- [US Stock Market](https://www.reddit.com/r/wallstreetbets/comments/xdb7ex/this_is_the_us_stock_market/)


## 4. Reflection

During the process, the part of analyzing word counts went well. I could improve on how to solve problems I met during the coding such as debugging, finding solutions to a certain error, and improving efficiency. During the process, I found it hard to find what is the exact problem and find the correlated solution. I began to be more familiar with how to solve errors that occurred in the code. I would still want to improve on efficiency and allocate the right amount of time. At the beginning of this project, I had no clear goal so I spent too much time watching online tutorials(practice file in Tests_and_Learn file)
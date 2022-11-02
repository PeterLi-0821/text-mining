# Part 3: Project Writeup and Reflection

## 1. Project Overview
The source I use is reddit. I found two links of reddit post with its sub-comments. I exported the contents extracted by the two links using praw and used pickle to create seperate data files for both links. I first analyze the document by counting the totol number of words and counted the most frequently appeared words to understand the data better. Then I used NLTK to know if the content is positive or nagative. I hope to create a program to quickly understand the opinion of certain topic from reddit users because it is hard to read all the comments from differnet users with different opinions. 

## 2. Implementation
Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice you did.

The first python file is used for getting data from reddit and convert the data into a file and store it. Everytime I try to use PRAW to get data from reddit, it took a while to do so. Therefore, storing data is important and saves lots of time. In analyze text part, I first open the data file, then use common code practiced in previouse works to get word counts. This is for understanding the text for further analysis. The new experience is using NLTK to get score of the comments. The result of the sentiment analysis is a dictinonay contains 4 keys and the only key I need is the conpound. So I wrote a for loop to get conpound scores for all the strings. Then I could get a average score of the overall post. 

## 3. Results
Present what you accomplished:

- If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
- If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.


## 4. Reflection
From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for testing? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?

During the process, the part of analyzing word counts went well. I could improve on how to solve problems I met during the coding such as debugging, finding sollutions to a certain error and improve efficiency. During the process, I found it hard to find what is the exact problem and find the corelated solution. I began to be more familiar with how to solve errors that occured in the code. I would still want to improve on efficiency and allocate right amount of time.
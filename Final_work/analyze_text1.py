#requirement
import praw
import pickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.downloader.download('vader_lexicon')

import random
import string
import sys
from unicodedata import category


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp =  filename

    if skip_header:
        skip_comment_header(fp)

    # strippables = string.punctuation + string.whitespace
    # via: https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in fp:
        if line.startswith('Personally, I think'): #there is no common same start for different comments, so I first read data and use startwith manually
            break

        line = line.replace('-', ' ')
        line = line.replace(
            chr(8212), ' '
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()

            # update the histogram
            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_comment_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def most_common(hist, excluding_stopwords=True):
    """Makes a list of word-freq pairs(tuples) in descending order of frequency.
    hist: map from word to frequency
    excluding_stopwords: a boolean value. If it is True, do not include any stopwords in the list.
    returns: list of (frequency, word) pairs
    """
    t = []
    stopwords = open('data/stopwords.txt', encoding='utf8')
    stopwords = process_file(stopwords, False)
    stopwords = list(stopwords.keys())
    # print(stopwords)

    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue

        t.append((freq, word))

    t.sort(reverse=True)
    return t


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)


#NLTK
def sentiment(comments): #this part has problem that I am not sure why. different result from Test\score.py
    """
    run sentiment to get the scores. The compound score is the sum of positive, negative & neutral scores which is then normalized between -1(most extreme negative) and +1 (most extreme positive).
    """
    scores = []
    for comment in (comments):
        score = SentimentIntensityAnalyzer().polarity_scores(comment)
        scores.append(score['compound']) 
        # return score['compound'] #all the compound scores for each comments
    avg = sum(scores)/len(scores) #this is average compound score of every strings from comments
    return avg

# if avg > 0, positive comment
#if avg < 0, negative comment



def main():
    with open('data\comment_us_stock_market_text.pickle','rb') as input_file:
        reloaded_copy_of_texts = pickle.load(input_file)
    hist = process_file(reloaded_copy_of_texts, skip_header=True)

    print('Total number of words:', total_words(hist))

    t = most_common(hist, False)

    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)
    print_most_common(hist, 20)

    print(sentiment(reloaded_copy_of_texts))


if __name__ == '__main__':
    main()
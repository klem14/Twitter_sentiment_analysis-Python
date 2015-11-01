import sys
import json
import re

def computeRatio(a,b):
    if b ==0:
       return a
    else:
        return float(a) / b

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    newSentiment = {}

    for line in tweet_file:
        parse = json.loads(line)

        if ('text' in parse) and ('lang' in parse) and (parse['lang']=='en'):
            unknownWord = []
            positiveMsg = 0
            negativeMsg = 0

            for word in parse["text"].split():
                word = re.sub(r'[^\w\s]','',word.encode('utf-8'))
                sentiment = scores.get(word,0)

                if sentiment > 0:
                    positiveMsg += sentiment
                elif sentiment < 0:
                        negativeMsg += sentiment
                else:
                        unknownWord.append(word)

                newWord = list(set(unknownWord))


            for word in newWord:
                if word not in newSentiment:
                    newSentiment[word] = (0,0)
                    newSentiment[word] = [sum(xrange) for xrange in zip(newSentiment[word],(positiveMsg,abs(negativeMsg)))]

    for i in newSentiment:
        print '%s %f' % (i, computeRatio(newSentiment[i][0],abs(newSentiment[i][1])))

if __name__ == '__main__':
    main()

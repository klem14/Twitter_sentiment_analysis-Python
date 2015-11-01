import sys
import json
import re

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    for line in tweet_file:
        parse = json.loads(line)

        if ('text' in parse) and (parse['lang']=='en'):
            sentiment = 0
            for word in parse["text"].split():
                sentiment += scores.get(re.sub(r'[^\w\s]','',word.encode('utf-8')),0)
            print sentiment
        else:
            print 0

if __name__ == '__main__':
    main()

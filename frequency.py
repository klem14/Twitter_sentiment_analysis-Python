import sys
import json
import re

def computeRatio(a,b):
    if b ==0:
       return a
    else:
        return float(a) / b

def main():
    tweet_file = open(sys.argv[1])

    frequence = {}

    for line in tweet_file:
        parse = json.loads(line)

        if ('text' in parse) and ('lang' in parse) and (parse['lang']=='en'):

            for word in parse["text"].split():
                word = word.encode('utf-8')
                if word not in frequence:
                    frequence[word] = 1
                else:
                    frequence[word] += 1

    total = sum(frequence.values())

    for word in frequence:
        print '%s %f' % (word,computeRatio(frequence[word],total))

if __name__ == '__main__':
    main()

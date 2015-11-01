import sys
import json
import re
import collections

def main():
    tweet_file = open(sys.argv[1])

    hash = {} # initialize an empty dictionary

    for line in tweet_file:
        parse = json.loads(line)

        if ('entities' in parse) and (parse['entities'] is not None):
            elem = parse['entities']

            if elem['hashtags'] is not None:
               hashtags = elem['hashtags']
               if len(hashtags)>0:
                    for i in hashtags:
                        tmp = i['text'].encode('utf-8')
                        hash[tmp] = hash.get(tmp,0) + 1

    for h,o in collections.Counter(hash).most_common(10):
        print '%s %i' % (h, o)

if __name__ == '__main__':
    main()

import sys
import json
import collections

def parse_hashtags(tweet_file):
    tweet_hashtags = []
    lines = [line.strip() for line in open(tweet_file) if line.strip()]
    data = [json.loads(line) for line in lines]
    for tweets in data:
        if u'entities' in tweets.keys():
            entities = tweets[u'entities']
            if u'hashtags' in entities.keys():
                hashtags = entities[u'hashtags']
                for hashtag in hashtags:
                    tweet_hashtags.append(hashtag['text'])
    return tweet_hashtags

def count_freq(tweet_text):
    freq = {}
    for content in tweet_text:
        if content in freq:
            freq[content] += 1
        else:
            freq[content] = 1
    return freq
        

def main():
    tweet_file = sys.argv[1]
    tweet_hashtags = parse_hashtags(tweet_file)
    tweet_freq = count_freq(tweet_hashtags)
    tweet_counter = collections.Counter(tweet_freq)
    for k, v in tweet_counter.most_common(10):
        print' %s, %f' %(k.encode('utf-8', 'ignore'), v)
    
if __name__ == '__main__':
    main()

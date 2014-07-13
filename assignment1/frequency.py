import sys
import json

def parse_tweets(tweet_file):
    tweet_text = []
    lines = [line.strip() for line in open(tweet_file) if line.strip()]
    data = [json.loads(line) for line in lines]
    for tweets in data:
        if u'text' in tweets.keys():
            tweet_text.append(tweets[u'text'])
    return tweet_text

def normalize(freq):
    total = sum(freq.values())
    for key in freq.keys():
        freq[key] = float(freq[key])/total
    return freq

def count_freq(tweet_text):
    freq = {}
    for content in tweet_text:
        words = content.split()
        for word in words:
            if not word in freq:
                freq[word] = 1
            else:
                freq[word] += 1
    return normalize(freq)
        

def main():
    tweet_file = sys.argv[1]
    tweet_text = parse_tweets(tweet_file)
    tweet_freq = count_freq(tweet_text)
    for key in tweet_freq.keys():
        print key, tweet_freq[key]

if __name__ == '__main__':
    main()

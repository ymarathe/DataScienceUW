import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def create_dict(afinn):
    afinnfile = open(afinn)
    scores = {}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def parse_tweets(tweet_file):
    tweet_text = []
    lines = [line.strip() for line in open(tweet_file) if line.strip()]
    data = [json.loads(line) for line in lines]
    for tweets in data:
        if u'text' in tweets.keys():
            tweet_text.append(tweets[u'text'])
    return tweet_text

def derive_sentiment(tweet_text, scores):
    sentiment = [0] * len(tweet_text)
    for index, content in enumerate(tweet_text):
        words = content.split()
        for word in words:
            if word in scores:
                sentiment[index] += scores[word]
    return sentiment

def derive_term_sentiment(tweet_text, scores, sentiment):
    term_scores = {}
    for index, content in enumerate(tweet_text):
        words = content.split()
        for word in words:
            if word not in scores:
                if word not in term_scores:
                    term_scores[word] = [sentiment[index], 1]
                else:
                    term_scores[word] = map(sum, zip(term_scores[word], [sentiment[index], 1]))
    #Deriving the final term sentiment
    for key in term_scores:
        val = term_scores[key]
        mod_val = float(val[0])/val[1]
        term_scores[key] = mod_val

    return term_scores
            
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = create_dict(sys.argv[1])
    tweet_text = parse_tweets(sys.argv[2])
    sentiment = derive_sentiment(tweet_text, scores)
    term_scores = derive_term_sentiment(tweet_text, scores, sentiment)
    for key in term_scores.keys():
        print key.encode('utf-8', 'ignore'), term_scores[key]

if __name__ == '__main__':
    main()

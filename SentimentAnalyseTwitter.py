import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'Your Customer Key'
consumer_secret= 'Your Customer Secret'

access_token='Your Access Token'
access_token_secret='Your Token Secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#verify the twitter
api=tweepy.API(auth)
api.verify_credentials()


#Get your twitter Information
myInfo=api.me()
#print(myInfo)
#api.update_status('Hi hi from Abo I have been posted!!!you can find me in your wall lol')



#Step 3 - Retrieve Tweets
public_tweets = api.search('Modi')
print(public_tweets)
#print(TextBlob(public_tweets.text))
#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:

    #print(tweet.text)


#Step 4 Perform Sentiment Analysis on Tweets


    analysis = TextBlob(tweet.text)

    print(analysis.sentiment)
#Value of polarity and subjectivity comes from Textblob package(for more info: sloria/TextBlob)
#print(TextBlob("unhappy").sentiment)

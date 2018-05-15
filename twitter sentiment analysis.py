import tweepy

from textblob import TextBlob



# Step 1 - Authenticate

consumer_key= 'qmOvjIW34bO466UKE3Jwx9tlH'

consumer_secret= 'n18ViE6pl5rdACcgDaqmLnnbINbOhxeNsTRd2lrt3U0Q7Y3iwd'



access_token='
1719844561-YlKYVuBl69xez6LlWXi3qiqNuZfrQdwcPd5AG9B'

access_token_secret='M0t1wiuKYtoP47SvNaHnBQ2JrhXbN85jGSWj79Rimj8j5'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)



api = tweepy.API(auth)



#Step 3 - Retrieve Tweets

public_tweets = api.search('Trump')







#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file

#and label each one as either 'positive' or 'negative', depending on the sentiment

#You can decide the sentiment polarity threshold yourself





for tweet in public_tweets:

    print(tweet.text)



    #Step 4 Perform Sentiment Analysis on Tweets

    analysis = TextBlob(tweet.text)

    print(analysis.sentiment)

    print("")

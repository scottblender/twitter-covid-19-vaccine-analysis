import snscrape.modules.twitter as sntwitter
import pandas as pd
# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid vaccine until:2021-05-24').get_items()):
    if i>100000:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.user.verified, tweet.user.followersCount, tweet.user.friendsCount, tweet.likeCount, tweet.retweetCount, tweet.quoteCount, tweet.user.created, tweet.user.location, tweet.user.displayname, tweet.lang, tweet.coordinates, tweet.place])
    
# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Verified', 'Followers Count', 'Friends Count', 'Like Count', 'Retweet Count', 'Quote Count', 'Created','Location','Display Name', 'Language', 'Coordinates', 'Place'])
tweets_df2.to_csv('First Extract.csv')

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid vaccine until:2021-05-13').get_items()):
    if i>100000:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.user.verified, tweet.user.followersCount, tweet.user.friendsCount, tweet.likeCount, tweet.retweetCount, tweet.quoteCount, tweet.user.created, tweet.user.location, tweet.user.displayname, tweet.lang, tweet.coordinates, tweet.place])
    
# Creating a dataframe from the tweets list above
tweets_df3 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Verified', 'Followers Count', 'Friends Count', 'Like Count', 'Retweet Count', 'Quote Count', 'Created','Location','Display Name', 'Language', 'Coordinates', 'Place'])
tweets_df3.to_csv('Second Extract.csv')

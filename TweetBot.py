import tweepy
import time

'''
Two keys inside OAuthHandler function are API key and API scecret Key from my twitter API app
keys inside set_access_token function are Access token key and Access token secret key from my twitter API app
'''
auth = tweepy.OAuthHandler(key1,key2)
auth.set_access_token(key1,key2)
             

api = tweepy.API(auth)  # provides access to our Twitter account using API

choice = """
Choose any of below options 
1.Show Home Time Line feeds
2.Show any User's Time Line feeds
3.Change profile picture
4.Display followers list
5.Follow back any followers of your account
6.Search any tweet with key word
"""

print(choice)

while True:
    user_option = str(input('Enter the option? '))

    def limit_handler(cursor):
        try:
            while True:
                yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(500)

    if (user_option == '1'):
        feed = api.home_timeline()  #Accessing home timeline feeds of user account and printing tweets in Text format
        for tweet in feed:
            print(tweet.text)

    elif (user_option == '2'):
        key_word = input('Enter User name of twitter account you want to see? ')
        feeds = api.user_timeline(key_word) #Accessing timeline feeds of other user account and printing tweets in Text format
        for tweet in feeds:
            print(tweet.text)

    elif (user_option == '3'):
        file_path = input('Enter the file path of the picture that you want to add as profile picturecfrom your System: ')
        api.update_profile_image(file_path)  

    elif (user_option == '4'):
        for follower in limit_handler(tweepy.Cursor(api.followers).items()):
            try:
                print(follower.name)  # Prints all of the followers account name 
            except StopIteration:
                break

    elif (user_option == '5'):
        string = input('Enter user name of your follower that you want to follow? ')
        for follower in limit_handler(tweepy.Cursor(api.followers).items()):
            try:
                if follower.name == string:  # Follow the user account which is specified
                    follower.follow()
            except StopIteration:
                break

    elif (user_option == '6'):
        search_string = input('Enter any key word to search for tweets in twitter feeds: ')  # Searches for key word in twitter feeds
        Number_of_tweets = 4  # If Tweets are found,program prints 4 tweets with key word searched and number can be modified
        for tweet in tweepy.Cursor(api.search, search_string).items(Number_of_tweets):
            try:
                tweet.favorite()
                print('You liked the tweet!')
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break
   

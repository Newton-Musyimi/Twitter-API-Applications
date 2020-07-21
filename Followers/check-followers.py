import tweepy, time

def getExceptionMessage(msg):
    words = msg.split(':')

    errorMsg = ""
    for index, word in enumerate(words):
        if index not in [0,1,2]:
            errorMsg = errorMsg + ' ' + word
    errorMsg = errorMsg.rstrip("\'}]")
    errorMsg = errorMsg.lstrip(" \'")
    errorMsg = errorMsg.rstrip('"')
    errorMsg = errorMsg.lstrip('"')
    errorMsg = errorMsg.rstrip(".")
    errorMsg = errorMsg + " !!!"
    

    return errorMsg

def main():
    consumer_key = "<Enter your consumer key here>"
    consumer_secret = "<Enter your consumer secret here>"
    access_token = "<Enter your access token here>"
    access_secret = "<Enter your access secret here>"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    name = "<Enter the username here>"
    try:
        followers = api.get_user(name).followers_count
        print(name+" has "+str(followers)+" followers.")
    except tweepy.error.TweepError as e:
        err = str(e.response.text)
        print(getExceptionMessage(err))

if __name__ == "__main__":
    main()
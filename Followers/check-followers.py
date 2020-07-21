import tweepy, time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
name = "<Enter the username here>"

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

try:
    followers = api.get_user(name).followers_count
    followers = name+" has "+str(followers)+" followers"
except tweepy.error.TweepError as e:
    err = str(e.response.text)

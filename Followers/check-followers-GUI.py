import tweepy, time
from tkinter import *

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

def getData():
    global label2
    name = E1.get()
    if(len(name)<=0):
        label2.config(text = "No username has been entered!")
        return
    try:        
        followers = api.get_user(str(name)).followers_count
        followers = name+" has "+str(followers)+" followers."
        label2.config(text = str(followers))
    except tweepy.error.TweepError as e:
        err = str(e.response.text)
        label2.config(text = (getExceptionMessage(err)))

def main():
    consumer_key = "<Enter your consumer key here>"
    consumer_secret = "<Enter your consumer secret here>"
    access_token = "<Enter your access token here>"
    access_secret = "<Enter your access secret here>"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    root = Tk()
    frame = Frame(root)
    frame.pack()

    label1 = Label(frame, text="Username")
    E1 = Entry(frame, bd = 5, width = 50, justify="center")
    label2 = Label(frame, text="Number of followers")
    submit = Button(frame, text ="Submit", command = getData)

    label1.pack()
    E1.pack()
    label2.pack()
    submit.pack(side = BOTTOM)
    root.title("Twitter Follower Count")
    root.mainloop()

if __name__ == "__main__":
    main()
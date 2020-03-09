import tweepy, json, random
from tweepy import OAuthHandler
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

consKey = "4TGPfg62pT76yWTnTE8INjJCL"
consSecret = "dkhHybaFTIAflvCVB5vFHQPu0eCHFQN1BIbpdx3hjt8q3aRqWy"
accessKey = "3061686882-PrrngsYGKlMV92KseseATs1Gjr5Yyucry61Lwl2"
accessSecret = "aLOiD62JKQg29mSoz6chfpLP7fbBpG4syMuaUvlAqe9J0"

auth = tweepy.OAuthHandler(consumer_key=consKey, consumer_secret=consSecret)

auth.set_access_token(accessKey, accessSecret)

api = tweepy.API(auth)
print("\n \n Make Sure that Font.tff is in the sameplace as CloudWordMaker.py \n \n")
cloudID = input("please enter your username : @")

item = api.get_user(cloudID)
print("name: " + item.name)
print("screen_name: " + item.screen_name)
print("description: " + item.description)
print("statuses_count: " + str(item.statuses_count))
number_of_tweets = item.statuses_count
print("friends_count: " + str(item.friends_count))
print("followers_count: " + str(item.followers_count))

tweets = tweepy.Cursor(api.user_timeline, id=cloudID).items(number_of_tweets)

import string
def preprocessing(text):
    
    for punc in string.punctuation: #Remove Punctuations
        text = text.replace(punc,"")
        
    for words in [' اگه ',' اگه ','من ',' من ','اون ',' اون ','این ',' این ',' از ','از ',' تا ','تا ',' نه ','نه ','در ',' در ','یا ',' یا ',' ای ','ای ',' شد ','شد ',' ها',' ها',' کرد',' هست',' ولی ','که ',' به ',' است ',' دارم ',' رو ',' هست',' هستن',' است ',' هم ',' یه ',' تو ',' من ',' ازش ',' بود',' دیگه ',' با ',' را ',' ما ','ما ',' چه ','چه ',' هر ',' توی ']:
        text = text.replace(words,"")


    for digit in ['0','1','2','3','4','5','6','7','8','9']: #Remove Digits
        text = text.replace(digit, "")

    for eng in ['a','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        text = text.replace(eng, "")

    cleared_text = " ".join(text.split()) #Remove Extra White Spaces

    return cleared_text
print("\n ****** \n Mate it's not stuck! just wait a little! \n ****** \n")
cloud = ""
for status in tweets:
    text= status.text
    text = preprocessing(text)
    if text:
        cloud = cloud + text

from arabic_reshaper import arabic_reshaper
from bidi.algorithm import get_display
cloudfinal = arabic_reshaper.reshape(cloud)
cloudfinal = get_display(arabic_reshaper.reshape(cloud))

print("\n ****** \n Press enter to continue if it's still stuck :))) \n ****** \n")

cloudwords = WordCloud(font_path="font.ttf",background_color="white").generate(cloudfinal)
plt.imshow(cloudwords,interpolation="bilinear")
plt.axis('off')
plt.show()
savename = input("gimme the file name to save! : ")
WordCloud.to_file(cloudwords,savename+".png")
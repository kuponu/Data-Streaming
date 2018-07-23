#import libraries
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json

ckey="Consumer Key"
csecret='Consumer Secret'
atoken='Access Token'
asecret='Access Token Secret'


class listener(StreamListener):
    #get the data
    def on_data(self,data):
            try:
                all_data=json.loads(data)
                tweet=all_data['text']
                loc=all_data['user']['location']
                Language=all_data['user']['lang']
                #print(str(time.time())+'\t' + tweet +'\t' + str(loc) + '\t' + str(Language))
                #print()
                newData= str(time.time())+ '\t' + tweet + '\t' + str(loc) + '\t' + str(Language)
                saveFile = open('WorldCupFinalData.txt','a', encoding='utf-8')
                saveFile.write(newData)
                saveFile.write('\n')
                saveFile.close()
                time.sleep(0.5)
                return True
            except Exception as e: #added to avoid termination due to timeout etc
                print('Failed Data,', str(e))
                time.sleep(7)
                pass
 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track=['WorldCupFinal', 'Fra','Cro','WorldCup']) #keyword search
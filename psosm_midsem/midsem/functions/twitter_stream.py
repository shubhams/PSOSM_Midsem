from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json


#consumer key, consumer secret, access token, access secret.
ckey="WhnybqNtvnzMuoCXqqY4oNPBl"
csecret="uL4lgB9PRVQjWEUWQN6ljxd4VRj05Our3Eb8Qsnw2UAfjhznyy"
atoken="3312126374-SvCJcWP5waeycYz9c214htWBlkVATxLOe28nRmK"
asecret="I9TiDSRhGvldSATAOjCD4S31Zwm80zRhPDqKh9KQOVe82"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        
        username = all_data["user"]["screen_name"]

        print '\ntime=',time.time(),', user=', username, 'tweet=\n', tweet, '\n'

        # print((username,tweet))
        
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
# =============Change track string to get desired tweets=============== 
twitterStream.filter(track=["ModiInSiliconValley"])
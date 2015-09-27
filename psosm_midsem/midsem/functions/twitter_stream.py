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
gterm=""

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet_id = all_data["id"]

        tweet = all_data["text"]

        created_time = all_data["created_at"]

        username = all_data["user"]["screen_name"]

        print '\ntime=',created_time,'id=', tweet_id,', user=', username, 'tweet=\n', tweet, '\n'

        append_file(gterm, data)
        # fw.write(data)

        return True

    def on_error(self, status):
        print status

def append_file(term, data):
	filename = term+'_search.json'
	fw = open(filename, "a")
	fw.write(data)

# ============Function to start streaming=============
def start_stream(term):
	global gterm
	gterm = term
	auth = OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)
	twitterStream = Stream(auth, listener())

	# =============Change track string to get desired tweets===============
	# twitterStream.filter(track=["ModiInSiliconValley"])
	twitterStream.filter(track=[term])


if __name__ == '__main__':
    start_stream("ModiInSiliconValley")

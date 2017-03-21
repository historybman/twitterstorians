# See instructions at https://github.com/sixohsix/twitter

from twitter import *
import simplejson as json

t = Twitter(
	auth = OAuth(token, token_secret, consumer_key, consumer_secret))

container = t.search.tweets(q="#twitterstorians")

print(json.dumps(container, sort_keys=True, indent=4 * ' '))




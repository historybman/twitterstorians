# See instructions at https://github.com/sixohsix/twitter
# Having trouble because the object returned at info is not just a standard Json file.

from twitter import *
# import simplejson as json
import json

# token = input("enter your token: ")
# token_secret = input("enter your token secret: ")
# consumer_key = input("enter your consumer_key: ")
# consumer_secret = input("enter your consumer_secret: ")

t = Twitter(auth = OAuth(token, token_secret, consumer_key, consumer_secret))


info = t.search.tweets(q="#twitterstorians")

# This is the method for pretty printing the list when using simplejson
# print(json.dumps(container, sort_keys=True, indent=4 * ' '))

# try looping through

# middle = container.read().decode()
info = json.loads(info)
print("User Count", len(info))

Count = 0
for item in info:
	print('Tweet:', item['text'])
	print('Handle:', item['screen_name'])
	print('Name:', item['name'])
	Count += 1
	print(Count)



import json
import oauth2 as oauth



#Get the access tokens and consumer tokens from apps.twitter.com
access_token = "520576491-bDvn5t92N4xtIV1QRiKHW87MN1fCGORSMKN2P8kY"
access_token_secret = "jrnnCkHsDn55yr8VroHW8bJFoK4Ufr6CFvPSOj81ttaO0"


consumer_key = "E3w6MqYOWEmpfGXS5kV5JlnVd"
consumer_secret = "we6kJD36BKXqaHE99tdAMXEVyiGLovaaM4zfKJRf1LC0Y26z9E"

consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
access = oauth.Token(key=access_token,secret=access_token_secret) 
client = oauth.Client(consumer,access)


#Get the URL from dev.twitter.com/rest/reference
timeline = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=Swaroop_Sriram&count=4"

response,data = client.request(timeline)

tweets = json.loads(data)
for tweet in tweets:
	print tweet["text"]
	# print data



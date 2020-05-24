import tweepy
import time


CONSUMER_KEY = 'Please enter your consumer_key.　あなたのconsumer_keyを入力してください。'
CONSUMER_SECRET = 'Please enter your consumer_secret.　あなたのconsumer_secretを入力してください。'
ACCESS_TOKEN = 'Please enter your access_token.　あなたのaccess_tokenを入力してください。'
ACCESS_SECRET = 'Please enter your access_secret.　あなたのaccess_secretを入力してください。'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

q_list = ["please enter words you wanna search for.　あなたが検索したいワードを入力してください。"]
count = "please enter how many numbers of tweets you wanna get.　あなたが取得したいtweet数を入力してください。"

for q in q_list:
    search_results = api.search(q=q, count=count)
    for result in search_results:
        tweet_id = result.id 
        user_id = result.user._json['id']
        try:
            api.create_favorite(tweet_id)
            api.create_friendship(user_id)
            time.sleep(20)
        except Exception as e:
            print(e)
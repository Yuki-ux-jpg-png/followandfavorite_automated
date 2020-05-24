import tweepy
import time

#xxxxxxxxxxxxxxxxxxxxxは各自取得したAPIをkeyを入れてください。
CONSUMER_KEY = '2avUeqXgYwZkOVGVWJUuksGrS'
CONSUMER_SECRET = 'N7ljlaLqqiTJef1M1jJvBmdlkgnEUlySLH1XqEzjlKi4vyNf1P'
ACCESS_TOKEN = '840838954597326848-dCQP7EpWW2VrBR11PPy1GBYFg7NGKWz'
ACCESS_SECRET = 'wUB9aNn6f3faNx85MMjhgjeBhVVHbETcEawRolZiBHOjj'
# インスタンス作成
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
# ここで検索をかけています。
# 検索したいワードをqという変数に入れます。今回は"プログラミング"でやってます。
# 取得したいTweet数をcountという変数に入れます。今回は100でやってます。
q_list = ["駆け出しエンジニア","python","data science"]
count = 3

for q in q_list:
    search_results = api.search(q=q, count=count)
    for result in search_results:
        tweet_id = result.id 
        user_id = result.user._json['id'] #ユーザーのidを取得
        try:
            api.create_favorite(tweet_id) #ファボする
            api.create_friendship(user_id) #フォローする
            time.sleep(20)
        except Exception as e:
            print(e)
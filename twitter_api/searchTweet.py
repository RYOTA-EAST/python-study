import tweepy, config

# 認証に必要なキーとトークン
API_KEY = config.API_KEY
API_SECRET = config.API_SECRET
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET

# APIの認証
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# キーワードからツイートを取得
api = tweepy.API(auth)
tweets = api.search(q=['"ねこプロ"'], count=10)

for tweet in tweets:
    print('-----------------')
    print(tweet.text)

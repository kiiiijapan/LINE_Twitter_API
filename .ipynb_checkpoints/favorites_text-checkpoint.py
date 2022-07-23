import datetime
import tweepy

def get_api():
    consumer_key = twitter_json['consumer_key']
    consumer_secret = twitter_json['consumer_secret']
    access_token = twitter_json['access_token']
    access_token_secret = twitter_json['access_token_secret']
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def my_favorites_tweet(api, num):
    #public_tweets = api.home_timeline()
    #me = api.verify_credentials()
    #n_followers = me.followers_count
    tweet_text = api.get_favorites()[num]._json['text']
    return tweet_text
    
def notify_message(message):
    LINE_NOTIFY_TOKEN = line_json['LINE_NOTIFY_TOKEN']
    url = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'
    }
    
    data = {
        'message':message
    }    
    requests.post(
    url,
    headers=headers,
    data=data)
    
def main():
    # TwitterAPIKEYとか取得
    api = get_key()
    
    # timezoneオブジェクトを指定
    # JST（日本標準時）に合わせるため+9時間の差分を指定
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    delta = datetime.timedelta(days=10)
    yesterday = now - delta
    
    # 「いいね」したツイートの個数取得（default=20）
    my_favorites_len = len(api.get_favorites())
    
    for i in range(my_favorites_len):
        tweet_time = api.get_favorites()[i]._json['created_at']
        # 取得したcreated_atがstr型なのでdatetime型に変換
        tweet_time = datetime.datetime.strptime(tweet_time, '%a %b %d %H:%M:%S %z %Y')
        # 「いいね」したツイートが今日のツイートだったらlineに送る
        if  tweet_time >= yesterday:
            # 「いいね」したツイートのテキスト取得
            favorites_text = my_favorites_tweet(api, i)
            # Lineに通知
            notify_message(favorites_text)
        else:
            pass

if __name__ == "__main__":
    main()
import tweepy
import configparser
import requests
import json

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.home_timeline()


# create dataframe
# columns = ['Time', 'User', 'Tweet']
# data = []
# for tweet in public_tweets:
#     data.append([tweet.created_at, tweet.user.screen_name, tweet.text])


# 打印推特消息
# for tweets in public_tweets:
#     print(tweets.text)


#发送钉钉消息
def dingmessage():
    # 请求的URL，WebHook地址
    webhook = "https://oapi.dingtalk.com/robot/send?access_token" \
              "=1f119a9b1d5717bbac43cb122be1e802a5dbbec592b6103a553c91e1ff1912fe "
    # 构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    # 构建请求数据
    tex = "上班注意安全，不要迟到"
    message = {
        "msgtype": "text",
        "text": {
            "content": tex
        },
        # "at": {
        #     "isAtAll": False
        # }
    }
    # 对请求的数据进行json封装
    message_json = json.dumps(message)
    # 发送请求
    info = requests.post(url=webhook, data=message_json, headers=header)
    # 打印返回的结果
    print(info.text)

dingmessage()

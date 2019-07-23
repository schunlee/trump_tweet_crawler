#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re

import datetime

import itchat
import requests
import schedule
import time
from sqlite_handler import init_table, insert, search
from translater import translate
from wechat import send_msg

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

__author__ = "bill.li"

if __name__ == '__main__':
    pass


    def get_recent_tweet(post_wechat=False):
        auth_url = 'https://twitter.com/realDonaldTrump'
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; LLD-AL00 Build/HONORLLD-AL00) AppleWebKit/537.36 (KHTML, like Gecko) MQQBrowser/7.3 Chrome/37.0.0.0 Mobile Safari/537.36"}
        session = requests.Session()

        session.request('GET', auth_url, headers=headers)
        cookie_obj = session.cookies
        cookie_list = list()
        for key, value in requests.utils.dict_from_cookiejar(cookie_obj).iteritems():
            cookie_list.append('{}={}'.format(key, value))
        cookie = '; '.join(cookie_list)
        headers.update({
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Host": "twitter.com",
            "Accept-Language": "en-us",
            "Accept-Encoding": "br, gzip, deflate",
            "Referer": "https://twitter.com/realDonaldTrump",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15",
            "Cookie": cookie,
            "X-Requested-With": "XMLHttpRequest",
            "X-Previous-Page-Name": "profile",
            "X-Overlay-Request": "true",
            "X-Twitter-Active-User": "yes"
        })

        resp = session.get(
            "https://twitter.com/realDonaldTrump",
            headers=headers).json()["page"]
        ids = re.findall(r'data-tweet-id=\"(\d+)\"', resp)

        for _id in ids:
            if not search(_id):
                tweet = session.get(
                    "https://twitter.com/realDonaldTrump/status/{id}?conversation_id={id}".format(id=_id),
                    headers=headers).json()
                tweet_time_str = re.findall(
                    r'realDonaldTrump/status/{}\" class=\"tweet-timestamp js-permalink js-nav js-tooltip\" title=\"(.*)\"\s+'
                    r'data-conversation-id'.format(
                        _id), tweet["page"])[0]
                print _id
                title = tweet["title"]
                translation = translate(tweet["title"])
                tweet_time = datetime.datetime.strptime(tweet_time_str, "%H:%M %p - %d %b %Y")
                insert(_id, tweet["title"], translate(tweet["title"]), tweet_time_str)
                msg_dict = {"content": title,
                       "translation": translation,
                       "time": str(tweet_time)
                       }
                msg = "【TIME】{}\n【CONTENT】{}\n【TRANSLATION】{}".format(msg_dict["time"],
                                                                      msg_dict["content"],
                                                                      msg_dict["translation"])
                if post_wechat:
                    # send_msg(msg)

                    # friend = itchat.search_friends("金小山")[0]["UserName"]
                    # itchat.
                    group = itchat.search_chatrooms('老李家')[0]["UserName"]
                    print itchat.send(msg, toUserName=group)
                    # friend.send(msg)

                    break
                print "###################"


    # init_table()
    itchat.auto_login(hotReload=True, enableCmdQR=False)
    get_recent_tweet(True)


    # def job():
    #     get_recent_tweet(True)
    #
    #
    # schedule.every(10).minutes.do(job)
    # # schedule.every().hour.do(job)
    #
    # while 1:
    #     schedule.run_pending()
    #     time.sleep(1)

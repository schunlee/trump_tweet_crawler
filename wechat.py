#!/usr/bin/python
# coding=utf-8
import json

# 获取access_token
import requests


# https://mp.weixin.qq.com/debug/cgi-bin/sandboxinfo?action=showinfo&t=sandbox/index
def get_access_token(appid, appsecret):
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appid, appsecret)
    data = requests.get(url).json()
    access_token = data['access_token']
    return access_token


def send_msg(iciba_everyday):
    appid = ""
    appsecret = ""

    for openid in ["orIO9wWe_Hw6JUxK__G1TECtuhz0","orIO9weLKbbFOnk2fu3rM-9Ub04I","orIO9wedXgymyBdilIRftHRrYzKs"]:
        msg = {
            "touser": openid,
            "msgtype": "text",
            "text":
                {
                    "content": "【TIME】{}\n【CONTENT】{}\n【TRANSLATION】{}".format(iciba_everyday["time"],
                                                                               iciba_everyday["content"],
                                                                               iciba_everyday["translation"]),
                }
        }
        json_data = json.dumps(msg, ensure_ascii=False).encode('utf-8')

        access_token = get_access_token(appid, appsecret)
        url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=%s' % str(access_token)
        result = requests.post(url, json_data).json()
        return result


if __name__ == '__main__':
    pass

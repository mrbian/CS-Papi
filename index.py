# coding=utf-8
import requests
import json
import flask
from task.index import task

_PAPI_MID = "1532165"

def officialLogin(appId, appSecret, token):
    url = "http://139.129.42.180:8000/oAuth/LoginToken?appId=%(appId)s&appSecret=%(appSecret)s&token=%(token)s" \
          % {"appId": appId, "appSecret": appSecret, "token": token}
    r = requests.get(url, timeout=10)
    data = json.loads(r.text)
    print data
    return data["msg"]["loginToken"]


def pushNews():
    nvlist = task(_PAPI_MID, 10, False)
    loginToken = officialLogin(appId="xb1878g98e7e87cc",appSecret="cgce381je9",token="OurEDA")
    url = "http://139.129.42.180:8000/oAuth/token/news/addOrModify"
    headers = {"LoginToken": loginToken}
    for video in nvlist:
        payload = {
            "content": "none",
            "author": "papi酱粉丝",
            "clickCount": video["play"],
            "img" : video["pic"],
            "title" : video["title"],
            "description" : video["description"],
            "priority" : 0,
            "files" : "[]",
            "id" : "none",
            "type" : 1,
            "redirectUrl" : video["redirectUrl"]
        }
        r = requests.post(url,data=payload,headers=headers)
        print r.text

pushNews()
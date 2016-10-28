# coding=utf-8
import requests
import json
import sys

_VIDEO_BASE_URL = "http://www.bilibili.com/video/av"

def isNew(aid):
    '''

    :param aid:
    :return:
    '''
    flag = True
    videoFile = open(sys.path[0] + "/video.json","r")
    data = json.load(videoFile)
    vlist = data["vlist"]
    for video in vlist :
        oaid = video["aid"]
        if aid == oaid :
            flag = False
            break
    videoFile.close()
    return flag

def getList(mid,pagesize,page,isAll):
    url = "http://space.bilibili.com/ajax/member/getSubmitVideos?mid=%(mid)s&pagesize=%(pagesize)d&page=%(page)d"\
          %{"pagesize":pagesize,"page":page,"mid" : mid}
    r = requests.get(url,timeout = 10)
    data = json.loads(r.text)
    vlist = data["data"]["vlist"]

    if(isAll) :
        return vlist

    nvlist = []                     # 新列表
    for video in vlist :
        aid = video["aid"]
        video["redirectUrl"] = "%(baseUrl)s%(aid)d"%{"baseUrl" : _VIDEO_BASE_URL,"aid" : aid}
        if isNew(aid) :             # 如果是新的则加入其中
            nvlist.append(video)
        else :
            break

    return nvlist

def cleanJson() :
    videoFile = open(sys.path[0] + "/video.json", "w")
    data = json.dumps({"vlist" : []})
    videoFile.write(data)
    videoFile.close()

def storeList(mid,count) :
    '''

    :param mid:
    :param count:
    :return:
    '''
    vlist = getList(mid,count,0,True)
    videoFile = open(sys.path[0] + "/video.json","w")
    data = json.dumps({"vlist": vlist})
    videoFile.write(data)
    videoFile.close()

def task(mid,count,isForce) :
    '''

    :param mid:
    :param count:
    :param isForce:
    :return:
    '''
    if isForce:
        cleanJson()
    nvlist = getList(mid,count,0,False)
    storeList(mid,count)
    return nvlist

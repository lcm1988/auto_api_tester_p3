#!/usr/bin/python3.5
#coding:utf-8
from conf.config import IS_DEBUG

#数据对比，根据数据结构递归对比
class JsonCompare():
    def __init__(self,expect_data,real_data,is_debug=IS_DEBUG):
        self.expect_data=expect_data
        self.real_data=real_data
        self.data_compare_result=[]#数据对比结果
        self.frame_cmpare_result=[]#结构对比结果
        self.defaultroot=''
        self.compare(expect_data,real_data,self.defaultroot)
        if is_debug:
            for i in self.data_compare_result:print(i)
            for i in self.frame_cmpare_result:print(i)

    def compare(self,expect_data,real_data,path='/'):
        try:
            if not isinstance(expect_data,(list,tuple,dict)):
                #if isinstance(real_data,unicode):real_data=real_data.encode('utf-8')
                if not expect_data==real_data:
                    self.data_compare_result.append('%s:预期值:%s%s,实际值:%s%s'%(path,str(expect_data),type(expect_data),str(real_data),type(real_data)))
            elif isinstance(expect_data,(list,tuple)):#list,tuple
                if not isinstance(real_data,(list,tuple)):
                    raise IndexError('实际数据不是list:%s'%path)#实际数据为非list/tuple类型
                for index,value in enumerate(expect_data):
                    try:
                        if index < len(real_data):
                            self.compare(value,real_data[index],'%s%s%d'%(path,'/下标:',index))
                        else:
                            raise IndexError('不存在的下标：%s%s%d'%(path,'/下标:',index))
                    except Exception as e:
                        if IndexError:
                            self.frame_cmpare_result.append('结构异常or数据缺失:%s'%e.args)
                        else:
                            self.frame_cmpare_result.append('未知异常:%s'%e.args)
            else:#dict
                if not isinstance(real_data,(dict)):
                    raise IndexError('实际数据不是dict:%s'%path)#实际数据为非dict类型
                for key,value in expect_data.items():
                    try:
                        if key in real_data.keys():
                            self.compare(value,real_data[key],'%s%s%s'%(path,'/键:',str(key)))
                        else:
                            raise IndexError('不存在的键：%s%s%s'%(path,'/键:',key))
                    except Exception as e:
                        if IndexError:
                            self.frame_cmpare_result.append('结构异常or数据缺失:%s'%e.args)
                        else:
                            self.frame_cmpare_result.append('未知异常:%s'%e.args)
        except Exception as e:
            self.frame_cmpare_result.append('未知异常:%s'%e.args)



if __name__=="__main__":
    import json
    a='''
    {
                "base": {
                    "title": "",
                    "img": "http://p8.qhimg.com/t01dba1cd198b98bb15.jpg",
                    "gif": "http://v1.cdn.naitang.tv/naitang-source-qa/dGVzdC9kcGljL3dlYnAvMjAxNzA3MTkvMTUwMDQ3OTE5OS9kMGVhMmY1ZTU0ODhhYTJlNTdhZjNjNzhjMmM2MTE2Yi53ZWJw",
                    "uri": "qhvideo://vapp.360.cn/videodetail?videoid=9139",
                    "tfuri": "toffee://com.toffee.video/videodetail?videoid=9139",
                    "playcount": "58",
                    "duration": "8",
                    "hottag": "",
                    "target": [],
                    "is_topic_top": 0,
                    "time": 1505904960
                },
                "id": "9139",
                "cover": "http://p8.qhimg.com/t01dba1cd198b98bb15.jpg",
                "auther": {
                    "userid": "20000002840",
                    "messageid": "toffee_20000002840",
                    "messagepasswd": "a9d7eb6240eb1603d6c4235ce153cc58",
                    "uidshow": "13791",
                    "title": "二奶",
                    "signature": "来奶糖，发现新的自己！",
                    "img": "http://quc.qhimg.com/dm/80_80_/t00df551a583a87f4e9.jpg",
                    "level": 6,
                    "leveltarget": {
                        "title": "Lv 6",
                        "fontcolor": "#B68526",
                        "background": "#FFF79D"
                    },
                    "verified": 0,
                    "uri": "qhvideo://vapp.360.cn/userdetail?userid=20000002840",
                    "tfuri": "toffee://com.toffee.video/userdetail?userid=20000002840",
                    "isFollow": 0,
                    "region": "外星人"
                },
                "music": {
                    "musicid": "6716",
                    "title": "爱情恰恰",
                    "img": "http://p0.qhimg.com/dm/80_80_/t01b4fbc5fccbb131ca.jpg",
                    "uri": "qhvideo://vapp.360.cn/musicdetail?musicid=6716",
                    "tfuri": "toffee://com.toffee.video/musicdetail?musicid=6716",
                    "desc": "爱情恰恰 - 陈小云"
                },
                "comment": {
                    "id": "9139",
                    "title": "1",
                    "uri": "qhvideo://vapp.360.cn/commentlist?commentid=9139",
                    "tfuri": "toffee://com.toffee.video/commentlist?commentid=9139",
                    "img": ""
                },
                "like": {
                    "title": "1",
                    "islike": 1,
                    "img": "",
                    "uri": "qhvideo://vapp.360.cn/userthumbsup?userid=20000002840&videoid=9139",
                    "tfuri": "toffee://com.toffee.video/userthumbsup?userid=20000002840&videoid=9139"
                },
                "share": {
                    "title": "@二奶 的奶糖短视频已经炸了！到底咋回事？",
                    "desc": "【奶糖】——发现新的自己 ^_^oo ~~ 15秒，打破平庸，爆炸的人生，精彩的你",
                    "img": "http://p8.qhimg.com/t01dba1cd198b98bb15.jpg",
                    "url": "http://toffee.app.test.tvfanqie.com/web/share/index?id=bYLsbJcaURH1US"
                },
                "shareIm": {
                    "targetName": "toffee_20000002840",
                    "notificationText": "我刚发布了一个新作品，想邀请你来为我点评一下！",
                    "desc": "我刚发布了一个新作品，想邀请你来为我点评一下！",
                    "videoCover": "http://p8.qhimg.com/t01dba1cd198b98bb15.jpg",
                    "videoUri": "toffee://com.toffee.video/videodetail?videoid=9139",
                    "label": "立即查看",
                    "musicName": "爱情恰恰-陈小云",
                    "title": "@二奶",
                    "target": []
                },
                "play": {
                    "videoid": "9139",
                    "playurl": "http://v1.cdn.naitang.tv/naitang-source-qa/dGVzdC92aWRlby9lbi8yMDE3MDcyMC8xNTAwNDgxOTk1L2QwZWEyZjVlNTQ4OGFhMmU1N2FmM2M3OGMyYzYxMTZiLm1wNA%3D%3D",
                    "playurl_key": "99384c45fdc5fa9f86c21a1f19a6a477",
                    "downloadurl": "http://v1.cdn.naitang.tv/naitang-source-qa/dGVzdC92aWRlby9lbi8yMDE3MDcyMC8xNTAwNDgxOTk1L2QwZWEyZjVlNTQ4OGFhMmU1N2FmM2M3OGMyYzYxMTZiLm1wNA%3D%3D"
                },
                "topic": {
                    "topicid": "0",
                    "title": "",
                    "uri": "qhvideo://vapp.360.cn/topicdetail?topicid=0",
                    "tfuri": "toffee://com.toffee.video/topicdetail?topicid=0"
                },
                "battle": {
                    "canbattle": "1",
                    "battleid": "",
                    "status": 0,
                    "battlewho": "",
                    "userid": "",
                    "tfuri": "",
                    "author": {
                        "userid": "",
                        "title": "",
                        "img": "",
                        "signature": "",
                        "tfuri": "",
                        "isFollow": 0,
                        "level": "1",
                        "leveltarget": {
                            "title": "Lv 1",
                            "fontcolor": "#B68526",
                            "background": "#FFF79D"
                        },
                        "verified": 0
                    },
                    "like": {
                        "title": "0",
                        "islike": 0,
                        "tfuri": ""
                    }
                },
                "control": {
                    "type": 1,
                    "postback": 1
                }
            }'''
    b='''
    {
                "base": {
                    "title": "",
                    "img": "http://p8.qhimg.com/t01cee2f34855cacd20.jpg",
                    "gif": "http://v1.cdn.naitang.tv/naitang-source-src/cmVsL2RwaWMvd2VicC8yMDE3MDcxOS8xNTAwNDY1MzU5L2IxYWJlNzAwZjE1MTQ4MzE3Yzc5MDUwMmFlODYwMGNhLndlYnA%3D",
                    "uri": "qhvideo://vapp.360.cn/videodetail?videoid=5362",
                    "tfuri": "toffee://com.toffee.video/videodetail?videoid=5362",
                    "playcount": "2465",
                    "duration": "10",
                    "hottag": "",
                    "target": [],
                    "is_topic_top": 0,
                    "time": 1505905026
                },
                "id": "5362",
                "cover": "http://p8.qhimg.com/t01cee2f34855cacd20.jpg",
                "auther": {
                    "userid": "20000002938",
                    "messageid": "toffee_20000002938",
                    "messagepasswd": "68ec3690643a1c39a8456d35632d3ffb",
                    "uidshow": "14080",
                    "title": "Es_浩雲",
                    "signature": "来奶糖，发现新的自己！",
                    "img": "http://quc.qhimg.com/dm/80_80_/t0137426301afacc0ee.jpg",
                    "level": 3,
                    "leveltarget": {
                        "title": "Lv 3",
                        "fontcolor": "#B68526",
                        "background": "#FFF79D"
                    },
                    "verified": 0,
                    "uri": "qhvideo://vapp.360.cn/userdetail?userid=20000002938",
                    "tfuri": "toffee://com.toffee.video/userdetail?userid=20000002938",
                    "isFollow": 0,
                    "region": "青岛市"
                },
                "music": {
                    "musicid": "4967",
                    "title": "Trouble To Love",
                    "desc": "Trouble To Love - 김댕,김관호,셀프 어쿠스틱",
                    "img": "http://p9.qhimg.com/dm/80_80_/t01223a05e4658ed49d.jpg",
                    "uri": "qhvideo://vapp.360.cn/musicdetail?musicid=4967",
                    "tfuri": "toffee://com.toffee.video/musicdetail?musicid=4967"
                },
                "comment": {
                    "id": "5362",
                    "title": "50",
                    "uri": "qhvideo://vapp.360.cn/commentlist?commentid=5362",
                    "tfuri": "toffee://com.toffee.video/commentlist?commentid=5362",
                    "img": ""
                },
                "like": {
                    "title": "60",
                    "islike": 0,
                    "img": "",
                    "uri": "qhvideo://vapp.360.cn/userthumbsup?userid=20000002938&videoid=5362",
                    "tfuri": "toffee://com.toffee.video/userthumbsup?userid=20000002938&videoid=5362"
                },
                "share": {
                    "title": "@Es_浩雲 的奶糖短视频已经炸了！到底咋回事？",
                    "desc": "【奶糖】——发现新的自己 ^_^oo ~~ 15秒，打破平庸，爆炸的人生，精彩的你",
                    "img": "http://p8.qhimg.com/t01cee2f34855cacd20.jpg",
                    "url": "http://www.naitang.tv/web/share/index?id=cofsaZQWTRP4Si"
                },
                "shareIm": {
                    "targetName": "toffee_20000002938",
                    "notificationText": "这个视频太有趣了，好东西怎么能忘记你呢，快来看看吧！",
                    "desc": "这个视频太有趣了，好东西怎么能忘记你呢，快来看看吧！",
                    "videoCover": "http://p8.qhimg.com/t01cee2f34855cacd20.jpg",
                    "videoUri": "toffee://com.toffee.video/videodetail?videoid=5362",
                    "label": "立即查看",
                    "musicName": "Trouble To Love-김댕,김관호,셀프 어쿠스틱"
                },
                "play": {
                    "videoid": "5362",
                    "playurl": "http://v1.cdn.naitang.tv/naitang-source-src/cmVsL3ZpZGVvL2VuLzIwMTcwNzE5LzE1MDA0NjY5NTUvYjFhYmU3MDBmMTUxNDgzMTdjNzkwNTAyYWU4NjAwY2EubXA0",
                    "playurl_key": "38f057eb408d3f108d8b4d8896fdf735",
                    "downloadurl": "http://v1.cdn.naitang.tv/naitang-source-src/cmVsL3ZpZGVvL2VuLzIwMTcwNzE5LzE1MDA0NjY5NTUvYjFhYmU3MDBmMTUxNDgzMTdjNzkwNTAyYWU4NjAwY2EubXA0"
                },
                "topic": {
                    "topicid": "0",
                    "title": "",
                    "uri": "qhvideo://vapp.360.cn/topicdetail?topicid=0",
                    "tfuri": "toffee://com.toffee.video/topicdetail?topicid=0"
                },
                "battle": {
                    "canbattle": "1",
                    "battleid": "",
                    "status": 0,
                    "battlewho": "",
                    "userid": "",
                    "tfuri": "",
                    "author": {
                        "userid": "",
                        "title": "",
                        "img": "",
                        "signature": "",
                        "tfuri": "",
                        "isFollow": 0,
                        "level": "1",
                        "leveltarget": {
                            "title": "Lv 1",
                            "fontcolor": "#B68526",
                            "background": "#FFF79D"
                        },
                        "verified": 0
                    },
                    "like": {
                        "title": "0",
                        "islike": 0,
                        "tfuri": ""
                    }
                },
                "control": {
                    "type": 1,
                    "postback": 1
                }
            }'''
    res=JsonCompare(json.loads(a),json.loads(b))







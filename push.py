import requests
import json
with open('result.txt','r',encoding='utf8') as origin_file:
    origin=origin_file.read()
origin=eval(origin)
pushdata={}
#推送渠道
pushdata['channel']='wechat'
# 具体请查看pushplus api文档https://www.pushplus.plus/doc/guide/api.html

# token=''
#检查token
if ('token' in locals().keys()) == True:
    pass
else:
    exit('+===============+\n| Token未定义！ |\n+===============+')
pushdata['content']=origin['result']
pushdata['title']=origin['title']+'啦'
pushdata['token']=token
push=json.loads(requests.post('http://www.pushplus.plus/send/',data=pushdata).text)
if push['code'] == 200:
    print('推送成功')
else:
    exit('推送失败：'+push['msg'])
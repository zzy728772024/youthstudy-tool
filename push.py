import requests
with open('result.txt','r',encoding='utf8') as origin_file:
    origin=origin_file.read()
origin=eval(origin)
pushdata={}
#检查token
if 'token' in locals().keys() == True:
    pass
else:
    exit('+===============+\n| Token未定义！ |\n+===============+')
pushdata['content']=origin['result']
pushdata['title']=origin['title']+'啦'
pushdata['token']=token
push=requests.post('http://www.pushplus.plus/send/',data=pushdata)

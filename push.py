import requests,json,main,time
with open('result.txt','r',encoding='utf8') as origin_file:
    origin=origin_file.read()
origin=eval(origin)
pushdata={}
#推送渠道
pushdata['channel']='wechat'
# 具体请查看pushplus api文档https://www.pushplus.plus/doc/guide/api.html

time.sleep(60)#平台统计有延迟
score_now=main.GetProfile.score()
score_add=score_now-origin['score']
if score_now < 100:
    score_need=100-score_now
elif score_now < 200:
    score_need=200-score_now
elif score_now < 500:
    score_need=500-score_now
elif score_now < 1000:
    score_need=1000-score_now
elif score_now < 5000:
    score_need=5000-score_now
else:
    score_need=0
sumup_output='\n此次执行增加了'+str(score_add)+'积分'+'\n当前为'+main.GetProfile.medal()+'，距离下一徽章还需'+str(score_need)+'积分'
# token=''
#检查token
if ('token' in locals().keys()) == True:
    pass
else:
    exit('+===============+\n| Token未定义！ |\n+===============+')
pushdata['content']=origin['result']+sumup_output
pushdata['title']=origin['title']+'啦'
pushdata['token']=token
push=json.loads(requests.post('http://www.pushplus.plus/send/',data=pushdata).text)
if push['code'] == 200:
    print('推送成功')
else:
    exit('推送失败：'+push['msg'])
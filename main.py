import requests,json
import time

# 获取时间戳
t = int(round(time.time()* 1000))

#如不使用github actions，请删除下方注释并手动设定xLitemallToken
#xLitemallToken=""

#检查xLitemallToken
if ('xLitemallToken' in locals().keys()) == True:
    pass
else:
    exit('+========================+\n| xLitemallToken未定义！ |\n+========================+')

headers = {
    'Host': 'youthstudy.12355.net',
    'Connection': 'keep-alive',
    'X-Litemall-Token': xLitemallToken,
    'X-Litemall-IdentiFication': 'young',
    'User-Agent': 'MicroMessenger',
    'Accept': '*/*',
    'Origin': 'https://youthstudy.12355.net',
    'X-Requested-With': 'com.tencent.mm',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://youthstudy.12355.net/h5/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}

headersj = {
    'Host': 'youthstudy.12355.net',
    'Connection': 'keep-alive',
    'X-Litemall-Token': xLitemallToken,
    'X-Litemall-IdentiFication': 'young',
    'User-Agent': 'MicroMessenger',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'X-Requested-With': 'com.tencent.mm',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://youthstudy.12355.net/h5/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}
#获取积分、徽章
class GetProfile:
    profile_dist=json.loads(requests.get('https://youthstudy.12355.net/saomah5/api/myself/get',headers=headers).text)
    if profile_dist['errmsg'] == '成功':
        def score():
            return(GetProfile.profile_dist['data']['entity']['score'])
        def medal():
            return(GetProfile.profile_dist['data']['entity']['medal']['name'])
score=GetProfile.score()
# (广东)每日签到
print("开始签到:")
mark = requests.get('https://youthstudy.12355.net/saomah5/api/young/mark/add', headers=headersj)
msg=json.loads(mark.text).get('msg')
print(msg)

# 青年大学习打卡
# 获得最新学习章节
latest = requests.get('https://youthstudy.12355.net/saomah5/api/young/chapter/new', headers=headersj)

chapterId=json.loads(latest.text).get('data').get('entity').get('id')
updateDate=json.loads(latest.text).get('data').get('entity').get('updateDate')
name=json.loads(latest.text).get('data').get('entity').get('name')

data = {
    'chapterId': chapterId,
}
# 打卡
print("打卡最新一期青年大学习:")
saveHistory = requests.post('https://youthstudy.12355.net/saomah5/api/young/course/chapter/saveHistory', headers=headers, data=data)
#print(saveHistory.text)

print("更新日期:",updateDate,"名称:",name,"打卡状态:",json.loads(saveHistory.text).get('msg'))


#“我要答题”

#获得题目
print("刷题:")
getList = requests.get('https://youthstudy.12355.net/saomah5/api/question/list', headers=headersj)
#print(getList.text)
questionlist=json.loads(getList.text).get("data").get("list")
submit_output=''
for questions in questionlist:
    #print(questions['id'])
    json_data = {
    'dataId': questions['id'],
    'commitDetails': [
        {
            'questionId': '1510063654195441665',
            'answer': '2,3,4',
            'active': True,
            'questionType': 1,
        },
        {
            'questionId': '1510063654187053058',
            'answer': '2,4',
            'active': True,
            'questionType': 1,
        },
        {
            'questionId': '1510063654203830274',
            'answer': '1,2,4',
            'active': True,
            'questionType': 1,
        },
        {
            'questionId': '1510063654208024578',
            'answer': '1,2,4',
            'active': True,
            'questionType': 1,
        },
        {
            'questionId': '1510063654191247361',
            'answer': '1,3',
            'active': True,
            'questionType': 1,
        },
    ],
    }
    #刷题
    submit = requests.post('https://youthstudy.12355.net/saomah5/api/question/submit/question', headers=headers, json=json_data)
    print(json.loads(submit.text).get('msg'),end="")
    submit_output=submit_output+json.loads(submit.text).get('msg')

#“广东共青团原创专区”
params = {
    'channelId': '1457968754882572290',
    'time': t,
}
getarticle = requests.get('https://youthstudy.12355.net/saomah5/api/article/get/channel/article', params=params, headers=headersj)
articleslist = json.loads(getarticle.text).get("data").get("entity").get("articlesList")
print("\n刷文章:")
addScore_output=''
for articles in articleslist:
    if articles['scoreStatus'] == False:
        params = {
            'id': articles['id'],
        }
        addScore = requests.get('https://youthstudy.12355.net/saomah5/api/article/addScore', params=params, headers=headersj)
        print(json.loads(addScore.text).get('msg'),end="")
        addScore_output=addScore_output+json.loads(addScore.text).get('msg')

#小结
score_now=GetProfile.score()
score_add=score_now-score
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
sumup_output='\n此次执行增加了'+str(score_add)+'积分'+'\n当前为'+GetProfile.medal()+'，距离下一徽章还需'+str(score_need)+'积分'
print(sumup_output)
'''
#往期课程
#获取季
getcourse = requests.get('https://youthstudy.12355.net/saomah5/api/young/course/list', headers=headersj)
courselist=json.loads(getcourse.text).get("data").get("list")
for course in courselist:
    #获取期
    #print(course['id'])
    params = {
        'id': course['id'],
    }
    getdetail = requests.get('https://youthstudy.12355.net/saomah5/api/young/course/detail', headers=headersj, params=params)
'''
output={}
output['title']=name+'签到'+json.loads(saveHistory.text).get('msg')
output['result']="更新日期:"+updateDate+"\n名称:"+name+"\n打卡状态:"+json.loads(saveHistory.text).get('msg')+"\n刷题：\n"+submit_output+"\n刷文章：\n"+addScore_output+sumup_output
with open('result.txt','a',encoding='utf8') as new_file:
    new_file.write(str(output))
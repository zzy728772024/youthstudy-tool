import requests,json
from main import headersj,headers
try:
    with open('result.txt','r',encoding='utf8') as origin_file:
        origin=origin_file.read()
        origin=eval(origin)
except:
    pass
#往期课程刷积分
#获取季
print("往期课程打卡:")
getChapterList = requests.get('https://youthstudy.12355.net/saomah5/api/young/course/list', headers=headersj)
chapterList=json.loads(getChapterList.text).get("data").get("list")
saveOldHistory_output=''
for chapter in chapterList:
    #获取期
    #print(chapter['id'])
    params = {
        'pid': chapter['id'],
    }
    getChapterDetail = requests.get('https://youthstudy.12355.net/saomah5/api/young/course/chapter/list', params=params, headers=headersj)
    chapterDetail=json.loads(getChapterDetail.text).get('data').get('list')
    for chapterId in chapterDetail:
        data = {
            'chapterId': chapterId['id'],
        }
        saveOldHistory = requests.post('https://youthstudy.12355.net/saomah5/api/young/course/chapter/saveHistory', headers=headers,data=data)
        print(json.loads(saveOldHistory.text).get('msg'),end="")
        saveOldHistory_output=saveOldHistory_output+json.loads(saveOldHistory.text).get('msg')
    origin['result']=origin['result']+saveOldHistory_output
    with open('result.txt','w+',encoding='utf8') as new_file:
        new_file.write(str(origin))
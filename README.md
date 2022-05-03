# 青年大学习工具
[![stars](https://img.shields.io/github/stars/Chenghow/youthstudy-tool.svg?label=Stars)](https://github.com/Chenghow/youthstudy-tool/stargazers)
[![forks](https://img.shields.io/github/forks/Chenghow/youthstudy-tool.svg?label=Forks)](https://github.com/Chenghow/youthstudy-tool/network/members)
[![GitHub contributors](https://img.shields.io/github/contributors/Chenghow/youthstudy-tool?label=Contributors)](https://github.com/Chenghow/youthstudy-tool/graphs/contributors)
## 支持
仅支持广东共青团智慧团建系统
## 目前支持的功能
- 青年大学习(广东)每日签到
- 青年大学习视频团课学习签到
- 青年大学习往期视频团课学习签到
- 学习频道薅羊毛
  - 自动答题赢积分(Beta)
  - 广东共青团原创专区刷积分(Beta)
- 推送执行结果(默认为微信)
## 使用方法
#### 注：以下所提到的“仓库”皆为你自己Fork的仓库
1. Fork本仓库
2. 在仓库的Settings-Secrets-Actions中分别添加以下两个Secrets并按实际情况填写
<<<<<<< Updated upstream
    - PUSHTOKEN（pushplus的token，如不需要推送可忽略）
    - XLITEMALLTOKEN（自行抓包获取，一般位于请求的Headers里）
=======
    - PUSHTOKEN（pushplus的token，**如不需要推送请将`.github/workflows/mark.yml`中的`push: true`字段改为`push: false`**）
    - MID（智慧团建-认证资料-生成电子团员证，点击最下方生成按钮。在团员证页面复制链接 应为：`https://tuan.12355.net/wechat/view/information/member_certification_generated.html?memberId=`**xxxxxx**`&showMemberAdditionNames=&showMemberRewardIds=&isShowAllFee=true` 其中xxxxxx即为mid）
    - ~~XLITEMALLTOKEN（自行抓包获取，**一般位于请求的Headers里**）**（仍可使用，不再推荐）**~~
>>>>>>> Stashed changes
3. 点击仓库的Actions，再点击“I understand my workflows, go ahead and enable them”的绿色按钮启用actions
4. 在侧边栏找到“GitHub Actions Youthstudy Bot”并点击，再点击右侧的“Enable workflow”启用此action
- 如本地使用请在main.py中手动指定xLitemallToken

## 未来支持的功能
- 学习频道薅羊毛
  - 我们爱学习
  - 团务小百科
- ~~微信登录API获取~~

## 特别感谢
[RnJ4/qndxx_batch_study](https://github.com/RnJ4/qndxx_batch_study)
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
## 使用须知
- 如使用github actions，请在你自己fork的仓库的Settings-Secrets-Actions中分别创建两个名为`XLITEMALLTOKEN`和`PUSHTOKEN`的Secret，并填写你自己的xLitemallToken和pushplus的token（如不使用pushplus请在.github/workflow/mark.yml中将`push: true`改为`push: false`）
- 如本地部署，请在main.py中设定xLitemallToken
## 未来支持的功能
- 学习频道薅羊毛
  - 我们爱学习
  - 团务小百科
- ~~微信登录API获取~~

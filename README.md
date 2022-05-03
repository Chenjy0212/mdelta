# modelta

Chen and Yang Lab Multi fork Development cell lineage tree alignment.

<!-- TOC -->

- [modelta](#modelta)
  - [01 Introduction](#01-introduction)
  - [02 Result](#02-result)
- [DecryptLogin](#decryptlogin)
- [Statements](#statements)
- [Support List](#support-list)
- [Practice with DecryptLogin](#practice-with-decryptlogin)
- [Install](#install)
      - [Preparation](#preparation)
      - [Pip install](#pip-install)
      - [Source code install](#source-code-install)
- [Quick Start](#quick-start)
- [Thanks List](#thanks-list)
- [Citation](#citation)
- [Projects in Charles_pikachu](#projects-in-charles_pikachu)
- [More](#more)
      - [WeChat Official Accounts](#wechat-official-accounts)

<!-- /TOC -->

## 01 Introduction

>pip install -i <https://test.pypi.org/simple/> modelta

Then you can use this function in your Python code. As shown below(**/modelta/test2.py**):

```python
import modelta
modelta.demola()
print(modelta.scoremat('modelta/ExampleFile/tree.nwk','modelta/ExampleFile/Name2Type.csv','modelta/ExampleFile/tree.nwk','modelta/ExampleFile/Name2Type.csv'))
```

## 02 Result

something output!
Matrix Node: 100%|███████████████████████████████████████████████████████████████████████████████████████| 121/121 [00:00<00:00, 20213.92it/s]
|Root2(col) & Root1(row) | 0,0,0 | 0,0,1|  0,0,2|  0,1|  0,2,0 | 0,2,1 |   1|   0,0  |0,2|     0|  root|
|  ----  | ----  |  ----  | ----  |  ----  | ----  |  ----  | ----  |  ----  | ----  |  ----  | ----  |
|0,0,0    |4.0|    0.0|   -1.0|  1.0|    0.0|   -2.0|  4.0|   2.0| -1.0  |-1.0|  -1.0|
|0,0,1|    2.0|    4.0|    0.0| -2.0|    0.0|   -1.0|  2.0|   2.0| -1.0|  -1.0|  -1.0|
|0,0,2|    2.0|    0.0|    4.0|  1.0|   -2.0|    2.0|  2.0|   2.0|  1.0|  -1.0|  -1.0|
|0,1|     -1.0|   -2.0|    1.0|  4.0|   -1.0|   -1.0| -1.0|  -1.0 |-1.0|  -1.0|  -1.0|
0,2,0|    2.0|    2.0|    1.0|  1.0|    4.0|   -1.0 | 2.0 |  0.0|  3.0  |-1.0  |-1.0
0,2,1|    0.0    |2.0  |  0.0| -2.0|    1.0|    4.0|  0.0|   0.0|  3.0|  -1.0 | -1.0|
1|        4.0   | 0.0|   -1.0|  1.0|    0.0|   -2.0|  4.0 |  2.0| -1.0|  -1.0|  -1.0|
0,0 |     2.0 |   2.0 |   2.0| -1.0|   -1.0|    0.0|  2.0|  12.0 | 1.0 |  9.0  | 8.0|
0,2   |   1.0    |1.0 |   0.0|  0.0|    3.0  |  3.0|  1.0 |  3.0  |8.0 |  4.0  | 3.0
0     |  -1.0|   -1.0|   -1.0| -1.0|   -1.0|   -1.0| -1.0  | 9.0 | 4.0  |24.0 | 23.0|
root |   -1.0   |-1.0   |-1.0| -1.0|   -1.0 |  -1.0| -1.0 |  8.0 | 3.0|  23.0|  28.0|

<div align ="center">
    <img src="./image/logoh.png" width="600"/>
</div>

<br />

[![docs](https://img.shields.io/badge/docs-latest-blue)](https://httpsgithubcomcharlespikachudecryptlogin.readthedocs.io/zh/latest/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/DecryptLogin)](https://test.pypi.org/project/modelta/)
[![PyPI](https://img.shields.io/pypi/v/DecryptLogin)](https://pypi.org/project/DecryptLogin)
[![license](https://img.shields.io/github/license/Chenjy0212/modelta.svg)](https://github.com/Chenjy0212/modelta/blob/main/LICENSE)
[![Github Stars](https://img.shields.io/github/stars/Chenjy0212?color=faf408&label=github%20stars&logo=github)](https://github.com/Chenjy0212)

Documents-CN:  <https://httpsgithubcomcharlespikachudecryptlogin.readthedocs.io/zh/latest/>

Documents-EN: <https://httpsgithubcomcharlespikachudecryptlogin.readthedocs.io/en/latest/>

# DecryptLogin

```
APIs for loginning some websites by using requests.
You can star this repository to keep track of the project if it's helpful for you, thank you for your support.
```

# Statements

```
This repo is created for learning python.
If I find that anyone leverage this project in an illegal way, I will delete this project immediately.

本项目仅供python爱好者学习使用, 若作者发现该项目以任何不正当方式被使用, 将立即删除该项目。
希望大家合理利用该项目🙂
```

# Support List

|    Websites     | PC Mode | Mobile Mode | ScanQR Mode |   Chinese Name    |
| :-------------: | :-----: | :---------: | :---------: | :---------------: |
|      weibo      |    ✓    |      ✓      |      ✓      |     新浪微博      |
|     douban      |    ✓    |      ✗      |      ✓      |       豆瓣        |
|     github      |    ✓    |      ✗      |      ✗      |      Github       |
|    music163     |    ✓    |      ✗      |      ✓      |    网易云音乐     |
|     zt12306     |    ✓    |      ✗      |      ✓      |   中国铁路12306   |
|     QQZone      |    ✗    |      ✗      |      ✓      |      QQ空间       |
|      QQQun      |    ✗    |      ✗      |      ✓      |       QQ群        |
|      QQId       |    ✗    |      ✗      |      ✓      |    我的QQ中心     |
|      zhihu      |    ✓    |      ✗      |      ✓      |       知乎        |
|    bilibili     |    ✓    |      ✓      |      ✓      |        B站        |
|     toutiao     |    ✗    |      ✗      |      ✓      |     今日头条      |
|     taobao      |    ✗    |      ✗      |      ✓      |       淘宝        |
|    jingdong     |    ✗    |      ✗      |      ✓      |       京东        |
|      ifeng      |    ✓    |      ✗      |      ✗      |      凤凰网       |
|      sohu       |    ✓    |      ✓      |      ✗      |       搜狐        |
|    zgconline    |    ✓    |      ✗      |      ✗      |    中关村在线     |
|      lagou      |    ✓    |      ✗      |      ✗      |      拉勾网       |
|     twitter     |    ✓    |      ✓      |      ✗      |       推特        |
|    eSurfing     |    ✗    |      ✗      |      ✓      |       天翼        |
|     renren      |    ✓    |      ✗      |      ✗      |      人人网       |
|    w3cschool    |    ✓    |      ✗      |      ✗      | W3Cschool(编程狮) |
|      fishc      |    ✓    |      ✗      |      ✗      |      鱼C论坛      |
|     youdao      |    ✓    |      ✗      |      ✗      |       有道        |
|    baidupan     |    ✓    |      ✗      |      ✗      |     百度网盘      |
|  stackoverflow  |    ✓    |      ✗      |      ✗      |   Stackoverflow   |
|     codalab     |    ✓    |      ✗      |      ✗      |      CodaLab      |
|      pypi       |    ✓    |      ✗      |      ✗      |       PyPi        |
|      douyu      |    ✗    |      ✗      |      ✓      |     斗鱼直播      |
|      migu       |    ✓    |      ✗      |      ✗      |     咪咕音乐      |
|      qunar      |    ✓    |      ✗      |      ✗      |    去哪儿旅行     |
|     mieshop     |    ✓    |      ✗      |      ✗      |     小米商城      |
|    mpweixin     |    ✓    |      ✗      |      ✗      |    微信公众号     |
|   baidutieba    |    ✗    |      ✗      |      ✓      |     百度贴吧      |
| dazhongdianping |    ✗    |      ✗      |      ✓      |     大众点评      |
|   jianguoyun    |    ✓    |      ✗      |      ✗      |      坚果云       |
|    cloud189     |    ✓    |      ✓      |      ✗      |     天翼云盘      |
|     qqmusic     |    ✗    |      ✗      |      ✓      |      QQ音乐       |
|    ximalaya     |    ✗    |      ✗      |      ✓      |     喜马拉雅      |
|   icourse163    |    ✗    |      ✓      |      ✗      |   中国大学MOOC    |
|  xiaomihealth   |    ✗    |      ✓      |      ✗      |     小米运动      |
|  tencentvideo   |    ✗    |      ✗      |      ✓      |     腾讯视频      |

# Practice with DecryptLogin

|          Project           |                        Introduction                        |                             code                             |           in Chinese            |
| :------------------------: | :--------------------------------------------------------: | :----------------------------------------------------------: | :-----------------------------: |
|        weiboMonitor        | [click](https://mp.weixin.qq.com/s/uOT1cGqXkOq-Hdc8TVnglg) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/weiboMonitor) |            微博监控             |
|          QQReport          | [click](https://mp.weixin.qq.com/s/dsVtEp_TFeyeSAAUn1zFEw) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/QQReports) |       生成QQ个人专属报告        |
| bilibiliDownloadUserVideos | [click](https://mp.weixin.qq.com/s/GaVW4_nbAaO0QvphI7QgnA) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/bilibiliDownloadUserVideos) |    下载B站指定UP主的所有视频    |
| NeteaseSongListDownloader  | [click](https://mp.weixin.qq.com/s/_82U7luG6jmV-xb8-Qkiew) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/NeteaseSongListDownloader) |      网易云个人歌单下载器       |
|  NeteaseListenLeaderboard  | [click](https://mp.weixin.qq.com/s/Wlf1a82oACc9N7zGezcy8Q) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/NeteaseListenLeaderboard) |      网易云个人听歌排行榜       |
|      userWeiboSpider       | [click](https://mp.weixin.qq.com/s/-3BDTZAE1x7nfCLNq2mFBw) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/userWeiboSpider) | 下载指定微博用户的所有微博数据  |
|       NeteaseSignin        | [click](https://mp.weixin.qq.com/s/8d7smUSzW2ds1ypZq-yeFw) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/NeteaseSignin) |       网易云音乐自动签到        |
|         weiboEmoji         | [click](https://mp.weixin.qq.com/s/QiPm4gyE8i5amR5gB3IbBA) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/weiboEmoji) |         微博表情包爬取          |
|        weiboSender         | [click](https://mp.weixin.qq.com/s/_aIY-iVj3xetfHQyMxflkg) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/weiboSender) |         大吼一声发微博          |
|          tbgoods           | [click](https://mp.weixin.qq.com/s/NhK9eeWNXv_wPnolccRR-g) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/tbgoods) |       淘宝商品数据小爬虫        |
|          jdgoods           | [click](https://mp.weixin.qq.com/s/LXheJveR248ZW4SP5F6fjw) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/jdgoods) |       京东商品数据小爬虫        |
|        delallweibos        | [click](https://mp.weixin.qq.com/s/E5Erg10FvyutEKaB_JGufA) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/delallweibos) |          批量删除微博           |
|         ClearQzone         | [click](https://mp.weixin.qq.com/s/Fj9MQXXRZ8wuKiX3Tytx8A) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/ClearQzone) |       批量删除QQ空间说说        |
|      NeteaseEveryday       | [click](https://mp.weixin.qq.com/s/tliFa5CYVEirMEyUj0jPbg) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/NeteaseEveryday) |   在终端看网易云每日歌曲推荐    |
|    NeteaseClickPlaylist    | [click](https://mp.weixin.qq.com/s/BpoO55I-jxAGO_Vv32khlA) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/NeteaseClickPlaylist) |     网易云音乐刷歌曲播放量      |
|       cloud189signin       | [click](https://mp.weixin.qq.com/s/tSLTSKDMzMAkP2deCjkanA) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/cloud189signin) |      天翼云盘自动签到+抽奖      |
|           moocdl           | [click](https://mp.weixin.qq.com/s/KsXU-pMvT8GzpPWVpcWIOA) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/moocdl) |       中国大学MOOC下载器        |
|    modifymihealthsteps     | [click](https://mp.weixin.qq.com/s/TQLM9GIW50UWAsKoXb7pzQ) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/modifymihealthsteps) |      修改小米运动中的步数       |
|         taobaosnap         | [click](https://mp.weixin.qq.com/s/vCZYtynHtQAOuQJHvjhpWA) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/taobaosnap) |          淘宝抢购脚本           |
|        jingdongsnap        | [click](https://mp.weixin.qq.com/s/-H8bwuUIPDi41d09tTlvRw) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/jingdongsnap) |          京东抢购脚本           |
|     bilibiliupmonitor      | [click](https://mp.weixin.qq.com/s/KjJLPcqHecK8T8LDVesxJQ) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/bilibiliupmonitor) |           B站UP主监控           |
|      bilibililottery       | [click](https://mp.weixin.qq.com/s/7kGjT48AOG_zB1v-cODgVw) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/bilibililottery) | B站监控关注的UP主并自动转发抽奖 |
|         weibowater         | [click](https://mp.weixin.qq.com/s/Avf169tvDNRLrgmrNj8jUw) | [click](https://github.com/CharlesPikachu/DecryptLogin/tree/master/examples/weibowater) |            微博水军             |

# Install

#### Preparation

- [Nodejs](https://nodejs.org/en/): Since some of the supported websites need to compile the js code, you should install the nodejs in your computer.

#### Pip install

```sh
run "pip install DecryptLogin"
```

#### Source code install

```sh
(1) Offline
Step1: git clone https://github.com/CharlesPikachu/DecryptLogin.git
Step2: cd DecryptLogin -> run "python setup.py install"
(2) Online
run "pip install git+https://github.com/CharlesPikachu/DecryptLogin.git@master"
```

# Quick Start

```python
from DecryptLogin import login

lg = login.Login()
infos_return, session = lg.douban()
infos_return, session = lg.github(username[email], password)
infos_return, session = lg.weibo()
infos_return, session = lg.music163(username[telephone/email], password)
infos_return, session = lg.zt12306(username[telephone], password)
infos_return, session = lg.QQZone()
infos_return, session = lg.QQQun()
infos_return, session = lg.QQId()
infos_return, session = lg.zhihu()
infos_return, session = lg.bilibili()
infos_return, session = lg.toutiao()
infos_return, session = lg.taobao()
infos_return, session = lg.jingdong()
infos_return, session = lg.ifeng(username, password)
infos_return, session = lg.sohu(username, password)
infos_return, session = lg.zgconline(username, password)
infos_return, session = lg.lagou(username, password)
infos_return, session = lg.twitter(username, password)
infos_return, session = lg.eSurfing()
infos_return, session = lg.renren(username, password)
infos_return, session = lg.w3cschool(username, password)
infos_return, session = lg.fishc(username, password)
infos_return, session = lg.youdao(username, password)
infos_return, session = lg.baidupan(username, password)
infos_return, session = lg.stackoverflow(username, password)
infos_return, session = lg.codalab(username, password)
infos_return, session = lg.pypi(username, password)
infos_return, session = lg.douyu()
infos_return, session = lg.migu(username, password)
infos_return, session = lg.qunar(username, password)
infos_return, session = lg.mieshop(username, password)
infos_return, session = lg.mpweixin(username, password)
infos_return, session = lg.baidutieba()
infos_return, session = lg.dazhongdianping()
infos_return, session = lg.jianguoyun(username, password)
infos_return, session = lg.cloud189(username, password)
infos_return, session = lg.qqmusic()
infos_return, session = lg.ximalaya()
infos_return, session = lg.icourse163(username, password)
infos_return, session = lg.xiaomihealth(username, password)
infos_return, session = lg.tencentvideo()
```

# Thanks List

|                    Author                    |    Time    |                  Contribution                   |
| :------------------------------------------: | :--------: | :---------------------------------------------: |
| @[skygongque](https://github.com/skygongque) | 2020-02-13 | add verification code processing in (weibo, pc) |

# Citation

If you use this project in your research, please cite this project.

```
@misc{decryptlogin2020,
    author = {Zhenchao Jin},
    title = {DecryptLogin: APIs for loginning some websites by using requests},
    year = {2020},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://github.com/CharlesPikachu/DecryptLogin}},
}
```

# Projects in Charles_pikachu

- [Games](https://github.com/CharlesPikachu/Games): Create interesting games by pure python.
- [DecryptLogin](https://github.com/CharlesPikachu/DecryptLogin): APIs for loginning some websites by using requests.
- [Musicdl](https://github.com/CharlesPikachu/musicdl): A lightweight music downloader written by pure python.
- [Videodl](https://github.com/CharlesPikachu/videodl): A lightweight video downloader written by pure python.
- [Pytools](https://github.com/CharlesPikachu/pytools): Some useful tools written by pure python.
- [PikachuWeChat](https://github.com/CharlesPikachu/pikachuwechat): Play WeChat with itchat-uos.
- [Pydrawing](https://github.com/CharlesPikachu/pydrawing): Beautify your image or video.
- [ImageCompressor](https://github.com/CharlesPikachu/imagecompressor): Image compressors written by pure python.
- [FreeProxy](https://github.com/CharlesPikachu/freeproxy): Collecting free proxies from internet.
- [Paperdl](https://github.com/CharlesPikachu/paperdl): Search and download paper from specific websites.
- [Sciogovterminal](https://github.com/CharlesPikachu/sciogovterminal): Browse "The State Council Information Office of the People's Republic of China" in the terminal.
- [CodeFree](https://github.com/CharlesPikachu/codefree): Make no code a reality.
- [DeepLearningToys](https://github.com/CharlesPikachu/deeplearningtoys): Some deep learning toys implemented in pytorch.
- [DataAnalysis](https://github.com/CharlesPikachu/dataanalysis): Some data analysis projects in charles_pikachu.
- [Imagedl](https://github.com/CharlesPikachu/imagedl): Search and download images from specific websites.
- [Pytoydl](https://github.com/CharlesPikachu/pytoydl): A toy deep learning framework built upon numpy.

# More

#### WeChat Official Accounts

*Charles_pikachu*  
![img](./docs/pikachu.jpg)

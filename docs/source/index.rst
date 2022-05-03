modelta
=======

Chen and Yang Lab Multi fork Development cell lineage tree alignment.

.. raw:: html

   <!-- TOC -->

-  `modelta <#modelta>`__

   -  `01 Introduction <#01-introduction>`__
   -  `02 Result <#02-result>`__

-  `DecryptLogin <#decryptlogin>`__
-  `Statements <#statements>`__
-  `Support List <#support-list>`__
-  `Practice with DecryptLogin <#practice-with-decryptlogin>`__
-  `Install <#install>`__ - `Preparation <#preparation>`__ - `Pip
   install <#pip-install>`__ - `Source code
   install <#source-code-install>`__
-  `Quick Start <#quick-start>`__
-  `Thanks List <#thanks-list>`__
-  `Citation <#citation>`__
-  `Projects in Charles_pikachu <#projects-in-charles_pikachu>`__
-  `More <#more>`__ - `WeChat Official
   Accounts <#wechat-official-accounts>`__

.. raw:: html

   <!-- /TOC -->

01 Introduction
---------------

   pip install -i https://test.pypi.org/simple/ modelta

Then you can use this function in your Python code. As shown
below(**/modelta/test2.py**):

.. code:: python

   import modelta
   modelta.demola()
   print(modelta.scoremat('modelta/ExampleFile/tree.nwk','modelta/ExampleFile/Name2Type.csv','modelta/ExampleFile/tree.nwk','modelta/ExampleFile/Name2Type.csv'))

02 Result
---------

something output! Matrix Node:
100%|███████████████████████████████████████████████████████████████████████████████████████\|
121/121 [00:00<00:00, 20213.92it/s] \|Root2(col) & Root1(row) \| 0,0,0
\| 0,0,1\| 0,0,2\| 0,1\| 0,2,0 \| 0,2,1 \| 1\| 0,0 \|0,2\| 0\| root\| \|
—- \| —- \| —- \| —- \| —- \| —- \| —- \| —- \| —- \| —- \| —- \| —- \|
\|0,0,0 \|4.0\| 0.0\| -1.0\| 1.0\| 0.0\| -2.0\| 4.0\| 2.0\| -1.0
\|-1.0\| -1.0\| \|0,0,1\| 2.0\| 4.0\| 0.0\| -2.0\| 0.0\| -1.0\| 2.0\|
2.0\| -1.0\| -1.0\| -1.0\| \|0,0,2\| 2.0\| 0.0\| 4.0\| 1.0\| -2.0\|
2.0\| 2.0\| 2.0\| 1.0\| -1.0\| -1.0\| \|0,1\| -1.0\| -2.0\| 1.0\| 4.0\|
-1.0\| -1.0\| -1.0\| -1.0 \|-1.0\| -1.0\| -1.0\| 0,2,0\| 2.0\| 2.0\|
1.0\| 1.0\| 4.0\| -1.0 \| 2.0 \| 0.0\| 3.0 \|-1.0 \|-1.0 0,2,1\| 0.0
\|2.0 \| 0.0\| -2.0\| 1.0\| 4.0\| 0.0\| 0.0\| 3.0\| -1.0 \| -1.0\| 1\|
4.0 \| 0.0\| -1.0\| 1.0\| 0.0\| -2.0\| 4.0 \| 2.0\| -1.0\| -1.0\| -1.0\|
0,0 \| 2.0 \| 2.0 \| 2.0\| -1.0\| -1.0\| 0.0\| 2.0\| 12.0 \| 1.0 \| 9.0
\| 8.0\| 0,2 \| 1.0 \|1.0 \| 0.0\| 0.0\| 3.0 \| 3.0\| 1.0 \| 3.0 \|8.0
\| 4.0 \| 3.0 0 \| -1.0\| -1.0\| -1.0\| -1.0\| -1.0\| -1.0\| -1.0 \| 9.0
\| 4.0 \|24.0 \| 23.0\| root \| -1.0 \|-1.0 \|-1.0\| -1.0\| -1.0 \|
-1.0\| -1.0 \| 8.0 \| 3.0\| 23.0\| 28.0\|

| |img|


|docs| |PyPI - Python Version| |PyPI| |license| |Github Stars|

Documents-CN:
https://httpsgithubcomcharlespikachudecryptlogin.readthedocs.io/zh/latest/

Documents-EN:
https://httpsgithubcomcharlespikachudecryptlogin.readthedocs.io/en/latest/

DecryptLogin
============

::

   APIs for loginning some websites by using requests.
   You can star this repository to keep track of the project if it's helpful for you, thank you for your support.

Statements
==========

::

   This repo is created for learning python.
   If I find that anyone leverage this project in an illegal way, I will delete this project immediately.

   本项目仅供python爱好者学习使用, 若作者发现该项目以任何不正当方式被使用, 将立即删除该项目。
   希望大家合理利用该项目🙂

Support List
============

=============== ======= =========== =========== =================
Websites        PC Mode Mobile Mode ScanQR Mode Chinese Name
=============== ======= =========== =========== =================
weibo           ✓       ✓           ✓           新浪微博
douban          ✓       ✗           ✓           豆瓣
github          ✓       ✗           ✗           Github
music163        ✓       ✗           ✓           网易云音乐
zt12306         ✓       ✗           ✓           中国铁路12306
QQZone          ✗       ✗           ✓           QQ空间
QQQun           ✗       ✗           ✓           QQ群
QQId            ✗       ✗           ✓           我的QQ中心
zhihu           ✓       ✗           ✓           知乎
bilibili        ✓       ✓           ✓           B站
toutiao         ✗       ✗           ✓           今日头条
taobao          ✗       ✗           ✓           淘宝
jingdong        ✗       ✗           ✓           京东
ifeng           ✓       ✗           ✗           凤凰网
sohu            ✓       ✓           ✗           搜狐
zgconline       ✓       ✗           ✗           中关村在线
lagou           ✓       ✗           ✗           拉勾网
twitter         ✓       ✓           ✗           推特
eSurfing        ✗       ✗           ✓           天翼
renren          ✓       ✗           ✗           人人网
w3cschool       ✓       ✗           ✗           W3Cschool(编程狮)
fishc           ✓       ✗           ✗           鱼C论坛
youdao          ✓       ✗           ✗           有道
baidupan        ✓       ✗           ✗           百度网盘
stackoverflow   ✓       ✗           ✗           Stackoverflow
codalab         ✓       ✗           ✗           CodaLab
pypi            ✓       ✗           ✗           PyPi
douyu           ✗       ✗           ✓           斗鱼直播
migu            ✓       ✗           ✗           咪咕音乐
qunar           ✓       ✗           ✗           去哪儿旅行
mieshop         ✓       ✗           ✗           小米商城
mpweixin        ✓       ✗           ✗           微信公众号
baidutieba      ✗       ✗           ✓           百度贴吧
dazhongdianping ✗       ✗           ✓           大众点评
jianguoyun      ✓       ✗           ✗           坚果云
cloud189        ✓       ✓           ✗           天翼云盘
qqmusic         ✗       ✗           ✓           QQ音乐
ximalaya        ✗       ✗           ✓           喜马拉雅
icourse163      ✗       ✓           ✗           中国大学MOOC
xiaomihealth    ✗       ✓           ✗           小米运动
tencentvideo    ✗       ✗           ✓           腾讯视频
=============== ======= =========== =========== =================

Practice with DecryptLogin
==========================

+----------------+----------------+----------------+----------------+
| Project        | Introduction   | code           | in Chinese     |
+================+================+================+================+
| weiboMonitor   | `clic          | `click <       | 微博监控       |
|                | k <https://mp. | https://github |                |
|                | weixin.qq.com/ | .com/CharlesPi |                |
|                | s/uOT1cGqXkOq- | kachu/DecryptL |                |
|                | Hdc8TVnglg>`__ | ogin/tree/mast |                |
|                |                | er/examples/we |                |
|                |                | iboMonitor>`__ |                |
+----------------+----------------+----------------+----------------+
| QQReport       | `clic          | `clic          | 生成           |
|                | k <https://mp. | k <https://git | QQ个人专属报告 |
|                | weixin.qq.com/ | hub.com/Charle |                |
|                | s/dsVtEp_TFeye | sPikachu/Decry |                |
|                | SAAUn1zFEw>`__ | ptLogin/tree/m |                |
|                |                | aster/examples |                |
|                |                | /QQReports>`__ |                |
+----------------+----------------+----------------+----------------+
| bilibiliDown   | `clic          | `click <       | 下载B站指定    |
| loadUserVideos | k <https://mp. | https://github | UP主的所有视频 |
|                | weixin.qq.com/ | .com/CharlesPi |                |
|                | s/GaVW4_nbAaO0 | kachu/DecryptL |                |
|                | QvphI7QgnA>`__ | ogin/tree/mast |                |
|                |                | er/examples/bi |                |
|                |                | libiliDownload |                |
|                |                | UserVideos>`__ |                |
+----------------+----------------+----------------+----------------+
| NeteaseSong    | `clic          | `click         | 网易云         |
| ListDownloader | k <https://mp. | <https://githu | 个人歌单下载器 |
|                | weixin.qq.com/ | b.com/CharlesP |                |
|                | s/_82U7luG6jmV | ikachu/Decrypt |                |
|                | -xb8-Qkiew>`__ | Login/tree/mas |                |
|                |                | ter/examples/N |                |
|                |                | eteaseSongList |                |
|                |                | Downloader>`__ |                |
+----------------+----------------+----------------+----------------+
| NeteaseLis     | `clic          | `click         | 网易云         |
| tenLeaderboard | k <https://mp. |  <https://gith | 个人听歌排行榜 |
|                | weixin.qq.com/ | ub.com/Charles |                |
|                | s/Wlf1a82oACc9 | Pikachu/Decryp |                |
|                | N7zGezcy8Q>`__ | tLogin/tree/ma |                |
|                |                | ster/examples/ |                |
|                |                | NeteaseListenL |                |
|                |                | eaderboard>`__ |                |
+----------------+----------------+----------------+----------------+
| u              | `clic          | `click <htt    | 下             |
| serWeiboSpider | k <https://mp. | ps://github.co | 载指定微博用户 |
|                | weixin.qq.com/ | m/CharlesPikac | 的所有微博数据 |
|                | s/-3BDTZAE1x7n | hu/DecryptLogi |                |
|                | fCLNq2mFBw>`__ | n/tree/master/ |                |
|                |                | examples/userW |                |
|                |                | eiboSpider>`__ |                |
+----------------+----------------+----------------+----------------+
| NeteaseSignin  | `clic          | `click <h      | 网易           |
|                | k <https://mp. | ttps://github. | 云音乐自动签到 |
|                | weixin.qq.com/ | com/CharlesPik |                |
|                | s/8d7smUSzW2ds | achu/DecryptLo |                |
|                | 1ypZq-yeFw>`__ | gin/tree/maste |                |
|                |                | r/examples/Net |                |
|                |                | easeSignin>`__ |                |
+----------------+----------------+----------------+----------------+
| weiboEmoji     | `clic          | `click         | 微博表情包爬取 |
|                | k <https://mp. |  <https://gith |                |
|                | weixin.qq.com/ | ub.com/Charles |                |
|                | s/QiPm4gyE8i5a | Pikachu/Decryp |                |
|                | mR5gB3IbBA>`__ | tLogin/tree/ma |                |
|                |                | ster/examples/ |                |
|                |                | weiboEmoji>`__ |                |
+----------------+----------------+----------------+----------------+
| weiboSender    | `clic          | `click         | 大吼一声发微博 |
|                | k <https://mp. | <https://githu |                |
|                | weixin.qq.com/ | b.com/CharlesP |                |
|                | s/_aIY-iVj3xet | ikachu/Decrypt |                |
|                | fHQyMxflkg>`__ | Login/tree/mas |                |
|                |                | ter/examples/w |                |
|                |                | eiboSender>`__ |                |
+----------------+----------------+----------------+----------------+
| tbgoods        | `clic          | `cl            | 淘宝           |
|                | k <https://mp. | ick <https://g | 商品数据小爬虫 |
|                | weixin.qq.com/ | ithub.com/Char |                |
|                | s/NhK9eeWNXv_w | lesPikachu/Dec |                |
|                | PnolccRR-g>`__ | ryptLogin/tree |                |
|                |                | /master/exampl |                |
|                |                | es/tbgoods>`__ |                |
+----------------+----------------+----------------+----------------+
| jdgoods        | `clic          | `cl            | 京东           |
|                | k <https://mp. | ick <https://g | 商品数据小爬虫 |
|                | weixin.qq.com/ | ithub.com/Char |                |
|                | s/LXheJveR248Z | lesPikachu/Dec |                |
|                | W4SP5F6fjw>`__ | ryptLogin/tree |                |
|                |                | /master/exampl |                |
|                |                | es/jdgoods>`__ |                |
+----------------+----------------+----------------+----------------+
| delallweibos   | `clic          | `click <       | 批量删除微博   |
|                | k <https://mp. | https://github |                |
|                | weixin.qq.com/ | .com/CharlesPi |                |
|                | s/E5Erg10Fvyut | kachu/DecryptL |                |
|                | EKaB_JGufA>`__ | ogin/tree/mast |                |
|                |                | er/examples/de |                |
|                |                | lallweibos>`__ |                |
+----------------+----------------+----------------+----------------+
| ClearQzone     | `clic          | `click         | 批量           |
|                | k <https://mp. |  <https://gith | 删除QQ空间说说 |
|                | weixin.qq.com/ | ub.com/Charles |                |
|                | s/Fj9MQXXRZ8wu | Pikachu/Decryp |                |
|                | KiX3Tytx8A>`__ | tLogin/tree/ma |                |
|                |                | ster/examples/ |                |
|                |                | ClearQzone>`__ |                |
+----------------+----------------+----------------+----------------+
| N              | `clic          | `click <htt    | 在终端看网易   |
| eteaseEveryday | k <https://mp. | ps://github.co | 云每日歌曲推荐 |
|                | weixin.qq.com/ | m/CharlesPikac |                |
|                | s/tliFa5CYVEir | hu/DecryptLogi |                |
|                | MEyUj0jPbg>`__ | n/tree/master/ |                |
|                |                | examples/Netea |                |
|                |                | seEveryday>`__ |                |
+----------------+----------------+----------------+----------------+
| Neteas         | `clic          | `c             | 网易云音       |
| eClickPlaylist | k <https://mp. | lick <https:// | 乐刷歌曲播放量 |
|                | weixin.qq.com/ | github.com/Cha |                |
|                | s/BpoO55I-jxAG | rlesPikachu/De |                |
|                | O_Vv32khlA>`__ | cryptLogin/tre |                |
|                |                | e/master/examp |                |
|                |                | les/NeteaseCli |                |
|                |                | ckPlaylist>`__ |                |
+----------------+----------------+----------------+----------------+
| cloud189signin | `clic          | `click <ht     | 天翼云盘       |
|                | k <https://mp. | tps://github.c | 自动签到+抽奖  |
|                | weixin.qq.com/ | om/CharlesPika |                |
|                | s/tSLTSKDMzMAk | chu/DecryptLog |                |
|                | P2deCjkanA>`__ | in/tree/master |                |
|                |                | /examples/clou |                |
|                |                | d189signin>`__ |                |
+----------------+----------------+----------------+----------------+
| moocdl         | `clic          | `c             | 中国           |
|                | k <https://mp. | lick <https:// | 大学MOOC下载器 |
|                | weixin.qq.com/ | github.com/Cha |                |
|                | s/KsXU-pMvT8Gz | rlesPikachu/De |                |
|                | pPWVpcWIOA>`__ | cryptLogin/tre |                |
|                |                | e/master/examp |                |
|                |                | les/moocdl>`__ |                |
+----------------+----------------+----------------+----------------+
| modif          | `clic          | `              | 修改小         |
| ymihealthsteps | k <https://mp. | click <https:/ | 米运动中的步数 |
|                | weixin.qq.com/ | /github.com/Ch |                |
|                | s/TQLM9GIW50UW | arlesPikachu/D |                |
|                | AsKoXb7pzQ>`__ | ecryptLogin/tr |                |
|                |                | ee/master/exam |                |
|                |                | ples/modifymih |                |
|                |                | ealthsteps>`__ |                |
+----------------+----------------+----------------+----------------+
| taobaosnap     | `clic          | `click         | 淘宝抢购脚本   |
|                | k <https://mp. |  <https://gith |                |
|                | weixin.qq.com/ | ub.com/Charles |                |
|                | s/vCZYtynHtQAO | Pikachu/Decryp |                |
|                | uQJHvjhpWA>`__ | tLogin/tree/ma |                |
|                |                | ster/examples/ |                |
|                |                | taobaosnap>`__ |                |
+----------------+----------------+----------------+----------------+
| jingdongsnap   | `clic          | `click <       | 京东抢购脚本   |
|                | k <https://mp. | https://github |                |
|                | weixin.qq.com/ | .com/CharlesPi |                |
|                | s/-H8bwuUIPDi4 | kachu/DecryptL |                |
|                | 1d09tTlvRw>`__ | ogin/tree/mast |                |
|                |                | er/examples/ji |                |
|                |                | ngdongsnap>`__ |                |
+----------------+----------------+----------------+----------------+
| bil            | `clic          | `click <https  | B站UP主监控    |
| ibiliupmonitor | k <https://mp. | ://github.com/ |                |
|                | weixin.qq.com/ | CharlesPikachu |                |
|                | s/KjJLPcqHecK8 | /DecryptLogin/ |                |
|                | T8LDVesxJQ>`__ | tree/master/ex |                |
|                |                | amples/bilibil |                |
|                |                | iupmonitor>`__ |                |
+----------------+----------------+----------------+----------------+
| b              | `clic          | `click <htt    | B站            |
| ilibililottery | k <https://mp. | ps://github.co | 监控关注的UP主 |
|                | weixin.qq.com/ | m/CharlesPikac | 并自动转发抽奖 |
|                | s/7kGjT48AOG_z | hu/DecryptLogi |                |
|                | B1v-cODgVw>`__ | n/tree/master/ |                |
|                |                | examples/bilib |                |
|                |                | ililottery>`__ |                |
+----------------+----------------+----------------+----------------+
| weibowater     | `clic          | `click         | 微博水军       |
|                | k <https://mp. |  <https://gith |                |
|                | weixin.qq.com/ | ub.com/Charles |                |
|                | s/Avf169tvDNRL | Pikachu/Decryp |                |
|                | rgmrNj8jUw>`__ | tLogin/tree/ma |                |
|                |                | ster/examples/ |                |
|                |                | weibowater>`__ |                |
+----------------+----------------+----------------+----------------+

Install
=======

Preparation
^^^^^^^^^^^

-  `Nodejs <https://nodejs.org/en/>`__: Since some of the supported
   websites need to compile the js code, you should install the nodejs
   in your computer.

Pip install
^^^^^^^^^^^

.. code:: sh

   run "pip install DecryptLogin"

Source code install
^^^^^^^^^^^^^^^^^^^

.. code:: sh

   (1) Offline
   Step1: git clone https://github.com/CharlesPikachu/DecryptLogin.git
   Step2: cd DecryptLogin -> run "python setup.py install"
   (2) Online
   run "pip install git+https://github.com/CharlesPikachu/DecryptLogin.git@master"

Quick Start
===========

.. code:: python

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

Thanks List
===========

+---------------------------+------------+---------------------------+
| Author                    | Time       | Contribution              |
+===========================+============+===========================+
| @\ `skygongque <https://  | 2020-02-13 | add verification code     |
| github.com/skygongque>`__ |            | processing in (weibo, pc) |
+---------------------------+------------+---------------------------+

Citation
========

If you use this project in your research, please cite this project.

::

   @misc{decryptlogin2020,
       author = {Zhenchao Jin},
       title = {DecryptLogin: APIs for loginning some websites by using requests},
       year = {2020},
       publisher = {GitHub},
       journal = {GitHub repository},
       howpublished = {\url{https://github.com/CharlesPikachu/DecryptLogin}},
   }

Projects in Charles_pikachu
===========================

-  `Games <https://github.com/CharlesPikachu/Games>`__: Create
   interesting games by pure python.
-  `DecryptLogin <https://github.com/CharlesPikachu/DecryptLogin>`__:
   APIs for loginning some websites by using requests.
-  `Musicdl <https://github.com/CharlesPikachu/musicdl>`__: A
   lightweight music downloader written by pure python.
-  `Videodl <https://github.com/CharlesPikachu/videodl>`__: A
   lightweight video downloader written by pure python.
-  `Pytools <https://github.com/CharlesPikachu/pytools>`__: Some useful
   tools written by pure python.
-  `PikachuWeChat <https://github.com/CharlesPikachu/pikachuwechat>`__:
   Play WeChat with itchat-uos.
-  `Pydrawing <https://github.com/CharlesPikachu/pydrawing>`__: Beautify
   your image or video.
-  `ImageCompressor <https://github.com/CharlesPikachu/imagecompressor>`__:
   Image compressors written by pure python.
-  `FreeProxy <https://github.com/CharlesPikachu/freeproxy>`__:
   Collecting free proxies from internet.
-  `Paperdl <https://github.com/CharlesPikachu/paperdl>`__: Search and
   download paper from specific websites.
-  `Sciogovterminal <https://github.com/CharlesPikachu/sciogovterminal>`__:
   Browse “The State Council Information Office of the People’s Republic
   of China” in the terminal.
-  `CodeFree <https://github.com/CharlesPikachu/codefree>`__: Make no
   code a reality.
-  `DeepLearningToys <https://github.com/CharlesPikachu/deeplearningtoys>`__:
   Some deep learning toys implemented in pytorch.
-  `DataAnalysis <https://github.com/CharlesPikachu/dataanalysis>`__:
   Some data analysis projects in charles_pikachu.
-  `Imagedl <https://github.com/CharlesPikachu/imagedl>`__: Search and
   download images from specific websites.
-  `Pytoydl <https://github.com/CharlesPikachu/pytoydl>`__: A toy deep
   learning framework built upon numpy.

More
====

WeChat Official Accounts
^^^^^^^^^^^^^^^^^^^^^^^^

| *Charles_pikachu*

.. |docs| image:: https://img.shields.io/badge/docs-latest-blue
   :target: https://httpsgithubcomcharlespikachudecryptlogin.readthedocs.io/zh/latest/
.. |PyPI - Python Version| image:: https://img.shields.io/pypi/pyversions/DecryptLogin
   :target: https://test.pypi.org/project/modelta/
.. |PyPI| image:: https://img.shields.io/pypi/v/DecryptLogin
   :target: https://pypi.org/project/DecryptLogin
.. |license| image:: https://img.shields.io/github/license/Chenjy0212/modelta.svg
   :target: https://github.com/Chenjy0212/modelta/blob/main/LICENSE
.. |Github Stars| image:: https://img.shields.io/github/stars/Chenjy0212?color=faf408&label=github%20stars&logo=github
   :target: https://github.com/Chenjy0212
.. |img| image:: ./image/logoh.png

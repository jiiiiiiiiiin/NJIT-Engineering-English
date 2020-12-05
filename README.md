# NJIT-Engineering-English
NJIT-Engineering-English

## 安装
 - 安装selenium `pip install selenium`
 - 下载[chromedriver](https://npm.taobao.org/mirrors/chromedriver/)
 
 ## 使用说明
 - 在`main.py`中写入你的账号。`English(username="", password="", browser=browser, unit=[1,2,3], shot=True)`
 - 运行`main.py`。
 - 在`/img`中即可看到完成截图。

## 说明
 - 适用于工程英语上册
 - 报错 `selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home`，下载chromedriver到 目录下面即可。
 - 报错 `selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 80`，chromedriver与chrome版本不对应,下载对应版本即可。
 - 密码正确，运行时提示密码错误，原因：没有使用校园玩或者WeNet。



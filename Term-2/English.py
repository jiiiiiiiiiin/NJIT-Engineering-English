# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import answer

unit_url_tmp = [
    "http://47.100.203.126:8081/StudentSTS/unitnav.aspx?BookId=30&UnitTreeid=4889",
    "http://47.100.203.126:8081/StudentSTS/unitnav.aspx?BookId=30&UnitTreeid=4922",
    "http://47.100.203.126:8081/StudentSTS/unitnav.aspx?BookId=30&UnitTreeid=4950",
    "http://47.100.203.126:8081/StudentSTS/unitnav.aspx?BookId=30&UnitTreeid=4980",
    "http://47.100.203.126:8081/StudentSTS/unitnav.aspx?BookId=30&UnitTreeid=5012",
    "http://47.100.203.126:8081/StudentSTS/unitnav.aspx?BookId=30&UnitTreeid=5043",
    "http://47.100.203.126:8081/StudentSTS/unitnav.aspx?BookId=30&UnitTreeid=5073",
    "http://47.100.203.126:8081/StudentSTS/unitnav.aspx?BookId=30&UnitTreeid=5102",
    "http://47.100.203.126:8081/StudentSTS/unitnav.aspx?BookId=30&UnitTreeid=5133",
    "http://47.100.203.126:8081/StudentSTS/unitnav.aspx?BookId=30&UnitTreeid=5161",
]


class English():
    def __init__(self, username, password, unit=None, auto=True, browser=None, shot=False, info=False):
        if not unit:
            unit = [i+1 for i in range(10)]

        if not browser:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            browser = webdriver.Chrome(chrome_options=chrome_options)
            pass

        self.shot = shot
        self.unit = unit
        self.username = username
        self.password = password
        self.browser = browser
        self.answer = answer.Answer_All()
        self.info=info

        self.browser.get('http://47.100.203.126:8081/Common/index.aspx')
        try:
            # 如果当前登陆的账号还在，退出账号
            self.browser.execute_script('document.getElementById("ctl00_lbtn_Quit").click()')
        except:
            pass



        self.unit_all = [self.answer.unit_1, self.answer.unit_2, self.answer.unit_3,
                         self.answer.unit_4, self.answer.unit_5, self.answer.unit_6,
                         self.answer.unit_7, self.answer.unit_8, self.answer.unit_9, self.answer.unit_10]
        if auto:
            self.taskAuto()
            print('*' * 10 + '{} is over!'.format(self.username))



    def taskLogin(self):
        js = "document.getElementById('ctl00_ContentPlaceHolder1_UcLogin1_txt_UserName').value='{username}';".format(username=self.username) + \
             "document.getElementById('ctl00_ContentPlaceHolder1_UcLogin1_txt_PassWord').value='{password}';".format(password=self.password) + \
             "document.getElementById('ctl00_ContentPlaceHolder1_UcLogin1_ibtn_ok').click();"
        self.browser.execute_script(js)
        self.browser.implicitly_wait(2) # 等待跳转
        self.browser.find_element_by_xpath('//a[@style="color:blue;"]').click() # 进入课堂
        self.browser.implicitly_wait(2) # 等待跳转 进入到单元选择页面
        self.url_unit = self.browser.current_url # 记录 unit页面的URL

    def taskEntryUnit(self, unit):
        self.browser.get(unit_url_tmp[unit-1])
        self.browser.implicitly_wait(2) # 等待跳转到 task 页面

    def taskFillWord(self, unit, taskName, url, answer):
        self.browser.get(url)
        self.browser.implicitly_wait(2)
        js = '''
               function task()
               {
                   var words = ''' + '{};'.format(answer) + '''
                   for(var i=0; i<''' + str(len(answer)) + '''; i++){
                       document.getElementsByName(String(i))[0].value=words[i];
                   }
               }
               task();
               '''
        self.browser.execute_script(js)

        try:
            self.browser.find_element_by_id('ctl00_ContentPlaceHolder1_submit').click()
            self.browser.switch_to.alert.accept()
        except:
            pass
        self.browser.implicitly_wait(2)
        if self.info:
            print('Unit {} {} is finished!'.format(unit, taskName))

    def taskFillText(self, unit, taskName, url, answer):
        self.browser.get(url)
        self.browser.implicitly_wait(2)

        js = '''
               function task()
               {
                   var words = ''' + '{};'.format(answer) + '''
                   var tmp = document.getElementsByTagName('textarea');
                   for(var i=0; i<''' + str(len(answer)) + '''; i++){
                       tmp[i].value=words[i];
                   }
               }
               task();
               '''

        self.browser.execute_script(js)

        try:
            self.browser.find_element_by_id('ctl00_ContentPlaceHolder1_submit').click()
            self.browser.switch_to.alert.accept()
        except:
            pass
        if self.info:
            print('Unit {} {} is finished!'.format(unit, taskName))

    def taskFillChoice(self, unit, taskName, url, answer):
        self.browser.get(url)
        self.browser.implicitly_wait(2)

        choice = []
        for i in range(len(answer)):
            choice.append(ord(answer[i]) - ord('A') + i * 4)
        js = '''
           function task()
           {
                var choice=''' + '{};'.format(choice) + '''
                var tmp = document.getElementsByTagName('input');
                var r=[];
                for(var i=0; i<tmp.length; i++){
                    if(tmp[i].type=="radio"){
                        r.push(tmp[i]);
                    }
                }
                for(var i=0;i<choice.length;i++){
                    r[choice[i]].click();
                }

           }
           task();
           '''
        self.browser.execute_script(js)
        try:

            self.browser.find_element_by_id('ctl00_ContentPlaceHolder1_submit').click()
            self.browser.switch_to.alert.accept()
        except:
            pass
        self.browser.implicitly_wait(2)
        if self.info:
            print('Unit {} {} is finished!'.format(unit, taskName))

    def taskEnd(self):
        self.browser.get(self.url_unit) # 跳转回 unit 选择页面

    def taskScreenShot(self):
        self.browser.get("http://47.100.203.126:8081/StudentSTS/DetailRecord.aspx")
        self.browser.get_screenshot_as_file('img/{}.png'.format(self.username))

    def end(self):
        self.browser.close() # 关闭浏览器

    def dis(self, num, data):
        self.taskEntryUnit(num)  # 进入相对应的单元
        for task in data:
            type = data[task][1]
            url = data[task][0]
            # print(url)
            ans = data[task][2]
            if type == 0:
                self.taskFillChoice(num, task, url, ans)
            elif type == 1:
                self.taskFillWord(num, task, url, ans)
            else:
                self.taskFillText(num, task, url, ans)
        self.browser.get(self.url_unit)

    def taskAuto(self):
        try:
            self.taskLogin() # 登陆
        except:
            print("{} 密码错误".format(self.username))
            return None
        for i in self.unit:
            if self.unit_all[i-1]:
                self.dis(i, self.unit_all[i-1])
                print("unit{} over".format(i))
            else:
                print("ERROR！当前单元为空！")
        self.taskEnd()
        if self.shot:
            self.taskScreenShot()# 有些顾客要求截图
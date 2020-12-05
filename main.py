from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from English import English


chrome_options = Options()
chrome_options.add_argument('--headless') # 无头模式
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.set_window_size(1200, 900)
print("开始工作...\n")

# 从这底下开始填 刷完的在每行前面加一个 “#”号 就可以注释掉
English(username="202190236", password="123456", browser=browser, unit=[1,2,3], shot=True)


browser.close()
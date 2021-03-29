from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from English import English


chrome_options = Options()
chrome_options.add_argument('--headless') # 无头模式
browser = webdriver.Chrome(options=chrome_options)
browser.set_window_size(1200, 900)
print("开始工作...")

#上册term=1,下册term=2
English(username="", password="123456", browser=browser, term=2, unit=[1,2,3,4,5,6,7,8,9,10], shot=True)


browser.close()

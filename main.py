from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from English import English


chrome_options = Options()
chrome_options.add_argument('--headless') # 无头模式
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.set_window_size(1200, 900)
print("开始工作...")


English(username="", password="123456", browser=browser, unit=[1,2,3], shot=True)


browser.close()

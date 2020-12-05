from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from English import English

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('--headless') # 无头模式
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.set_window_size(1200, 900)

    English(username='', password='', browser=browser, unit=[1,2,3,4,5,6,7], shot=True, info=True)

    browser.close()

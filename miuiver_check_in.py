from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
import requests
from urllib import parse
from selenium.webdriver.common.by import By


#通过bark推送结果,填写你的推送地址
bark_url = "you_bark_url"

os.system("killall -9 chrome")
os.system("killall -9 chromedriver")


#填写你的用户名/密码
email = ""
password = ""
notice_title = "miuiver签到"

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://miuiver.com/wp-login.php")

time.sleep(1)
driver.find_element(By.ID, 'user_login').send_keys(email)
time.sleep(1)
driver.find_element(By.ID, 'user_pass').send_keys(password)
time.sleep(1)
driver.find_element(By.ID, 'wp-submit').click()

print(driver.title)

time.sleep(3)

button_text = driver.find_element(By.XPATH, '//*[@id="userProfile"]/div[1]/header/a').text

if button_text == "已签到":
    print("今日已签到")
else:
    print('正在进行签到')
    driver.find_element(By.CLASS_NAME,'usercheck.erphp-checkin').click()
    time.sleep(3)

driver.refresh()
integral_text = driver.find_element(By.XPATH, '//*[@id="userProfile"]/div[1]/div/div[3]/div/p/span').text
button_text = driver.find_element(By.XPATH, '//*[@id="userProfile"]/div[1]/header/a').text

checkin_result = ("_____签到结果______\n签到情况： {}\n{}".format(button_text, integral_text))

print(checkin_result)

requests.get(f"{bark_url}/{notice_title}/{checkin_result}")

driver.quit()

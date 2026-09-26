from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import time

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 自动管理Chrome和driver版本
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

try:
    driver.get("https://laowang.vip")
    time.sleep(4)

    driver.find_element(By.LINK_TEXT, "登录").click()
    time.sleep(3)

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "submit").click()
    time.sleep(5)

    # dzsign签到页面
    driver.get("https://laowang.vip/plugin.php?id=dzsign:dzsign")
    time.sleep(4)

    sign_btn = driver.find_element(By.XPATH, '//button[contains(text(),"签到")]')
    sign_btn.click()
    time.sleep(3)

    print("✅签到脚本执行完成")

except Exception as e:
    print(f"❌出错：{e}")
finally:
    driver.quit()

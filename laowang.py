from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time

# 读取GitHub Secrets里的账号密码
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# 无头Chrome配置（GitHub云端运行用）
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=chrome_options)

try:
    # 打开老王论坛首页
    driver.get("shturl.cc/2xMKKbOZqZwbavb4tYv")
    time.sleep(4)

    # 点击登录入口（Discuz顶部登录按钮）
    driver.find_element(By.LINK_TEXT, "登录").click()
    time.sleep(3)

    # 填写账号密码，Discuz表单name="username" 和 name="password"
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)

    # 提交登录表单
    driver.find_element(By.NAME, "submit").click()
    time.sleep(5)

    # 登录完成，访问签到页面（dz论坛签到插件一般是plugin.php）
    driver.get("https://laowang.vip/plugin.php?id=dzsign:dzsign")
    time.sleep(4)

    # 点击签到按钮
    sign_btn = driver.find_element(By.XPATH, '//button[contains(text(),"签到")]')
    sign_btn.click()
    time.sleep(3)

    print("✅签到脚本执行完成")

except Exception as e:
    print(f"❌出错：{e}")
finally:
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# 開啟網頁
#driver.get("https://www.google.com")
driver.get("https://tixcraft.com/")

time.sleep(5)

#ctrl+shift+i查看網頁原始代碼
#會員登入
login_button = driver.find_element(By.CLASS_NAME, "justify-content-center")
login_button.click()
fb_button = driver.find_element(By.ID, "facebook")
fb_button.click()


time.sleep(5)



# search_box = driver.find_element("name", "q")  # "q" 是 Google 搜尋框的 name 屬性
# search_box.send_keys("Selenium Python")  # 在搜尋框中輸入 "Selenium Python"
# search_box.send_keys(Keys.RETURN)  # 模擬按下 Enter 鍵

# 記得在完成操作後關閉瀏覽器
#driver.quit()

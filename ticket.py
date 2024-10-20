from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

# 開啟網頁
#driver.get("https://www.google.com")
#driver.get("https://tixcraft.com/activity/game/24_jaychou")
driver.get("https://tixcraft.com/activity/game/25_casty")
driver.maximize_window()

if(driver.find_element(By.CLASS_NAME, "banner-content")):
    reject_button = driver.find_element(By.ID, "onetrust-reject-all-handler").click()

time.sleep(1)

# ctrl+shift+i查看網頁原始代碼
# 會員登入
login_button = driver.find_element(By.CLASS_NAME, "justify-content-center").click()
fb_button = driver.find_element(By.ID, "facebook").click()

# login facebook
account_fill = driver.find_element(By.ID, "email")
account_fill.send_keys("your email")
password_fill = driver.find_element(By.ID, "pass")
password_fill.send_keys("tour password")
login = driver.find_element(By.NAME, "login").click()
continue_button = driver.find_elements(By.CSS_SELECTOR, '[aria-label="以XX的身分繼續"]')
continue_button[0].click()

#不斷刷新直到下拉式選單出現

#滾動視窗到底部
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(5)

# choose day
select_day = driver.find_elements(By.TAG_NAME, value="Option")
i=0
while i < len(select_day):
    if(select_day[i].text == "2025/03/22 (六)"):
        select_day[i].click
    i=i+1

buy_button = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary text-bold m-0"]').click()

#choose zone & ticket num
select_zone = driver.find_element(By.CLASS_NAME, "select_form_a").click()
select_num = Select(driver.find_element(By.ID, "TicketForm_ticketPrice_02"))
select_num.select_by_index(2)

# verifyCode
verifyCode_fill = driver.find_element(By.ID, "TicketForm_verifyCode")
verifyCode_fill.send_keys("ai圖片辨識結果回傳")
checkbox = driver.find_element(By.ID, "TicketForm_agree").click()
confirm_button = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary btn-green"]').click()
confirm_order_button = driver.find_element(By.ID, "submitButton").click()


time.sleep(100)

# 關閉瀏覽器
#driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()

# 開啟售票網址(拓元)
driver.get("https://")

driver.maximize_window()

# ctrl+shift+i查看網頁原始代碼

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "banner-content"))
    )
    reject_button = driver.find_element(By.ID, "onetrust-reject-all-handler").click()
except NoSuchElementException:
    print("no banner")
    
# 會員登入
login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "justify-content-center"))
    ).click()
fb_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "facebook"))
    ).click()

# login facebook
account_fill = driver.find_element(By.ID, "email")
account_fill.send_keys("your email")
password_fill = driver.find_element(By.ID, "pass")
password_fill.send_keys("your password")
login = driver.find_element(By.NAME, "login").click()
continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="以xx的身分繼續"]'))
    ).click()

#不斷刷新頁面直到立即購買按鈕出現
#待新增功能：指定刷新時間(ex：11:59)
while True:
    try:
        # 找到並點擊按鈕
        buy_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="btn btn-primary text-bold m-0"]'))
        )
        buy_button.click()
        break  # 跳出循環
    except Exception as e:
        driver.refresh()

# choose zone & ticket num
# 驗證碼輸入錯誤後網頁重整這些都要重填(待改)
if(driver.find_element(By.CLASS_NAME, "select_form_a")):
    select_zone = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "select_form_a"))   #票有剩才有得選
    ).click()

select_num = Select(driver.find_element(By.CSS_SELECTOR, '[class="form-select mobile-select"]')) 
select_num.select_by_index(2) #兩張

# verifyCode
# verifyCode_img = driver.find_element(By.ID, "TicketForm_verifyCode-image")
# verifyCode_img.screenshot('captcha.png')
# 辨識完驗證碼後回傳結果
# # verifyCode_fill.send_keys(captcha_text)
# verifyCode_fill.send_keys(captcha_input)

if(driver.find_element(By.ID, "TicketForm_agree")):
    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "TicketForm_agree"))  
    ).click()

verifyCode_fill = driver.find_element(By.ID, "TicketForm_verifyCode")
captcha_input = input('print')

# if(driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary btn-green"]')):
#     confirm_button = WebDriverWait(driver, 5).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="btn btn-primary btn-green"]')) 
#     ).click()

#會跑一段時間

#付款頁面
#無連續座位會跳回選位子
# try:
#     # Select payment and delivery methods
#     Transfer_money = WebDriverWait(driver, ).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="form-check-input"]'))   
#     ).click()

#     confirm_order_button = WebDriverWait(driver, 5).until(
#         EC.element_to_be_clickable((By.ID, "submitButton"))   
#     ).click()
# except Exception as e:
#     print(f"發生錯誤: {e}")

# 關閉瀏覽器
# driver.quit()

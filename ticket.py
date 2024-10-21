from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
# from PIL import Image, ImageFilter, ImageEnhance
# import pytesseract
# import cv2
# import numpy as np

# 替換為你的 Tesseract 安裝路徑
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows 示例


driver = webdriver.Chrome()

# 開啟網頁
#driver.get("https://tixcraft.com/activity/game/24_jaychou")
driver.get("https://tixcraft.com/activity/game/24_p12tienmu")
driver.maximize_window()

# ctrl+shift+i查看網頁原始代碼

try:
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "banner-content"))
    )
    reject_button = driver.find_element(By.ID, "onetrust-reject-all-handler").click()
except NoSuchElementException:
    print("no banner")
    
# 會員登入
login_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "justify-content-center"))
    ).click()
fb_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.ID, "facebook"))
    ).click()

# login facebook
account_fill = driver.find_element(By.ID, "email")
account_fill.send_keys("your email")
password_fill = driver.find_element(By.ID, "pass")
password_fill.send_keys("your password")
login = driver.find_element(By.NAME, "login").click()
continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="以XX的身分繼續"]'))
    ).click()

#不斷刷新頁面直到立即購買按鈕出現
while True:
    try:
        # 嘗試找到並點擊按鈕
        buy_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="btn btn-primary text-bold m-0"]'))
        )
        buy_button.click()
        break  # 跳出循環
    except Exception as e:
        driver.refresh()

# choose zone & ticket num
if(driver.find_element(By.CLASS_NAME, "select_form_a")):
    select_zone = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "select_form_a"))   #票有剩才有得選
    ).click()

select_num = Select(driver.find_element(By.CSS_SELECTOR, '[class="form-select mobile-select"]')) 
select_num.select_by_index(2) #兩張

# # verifyCode
# verifyCode_img = driver.find_element(By.ID, "TicketForm_verifyCode-image")
# verifyCode_img.screenshot('captcha.png')

# # 使用 OpenCV 進行更佳的預處理
# captcha_image_cv = cv2.imread('captcha.png')

# # 轉換為 HSV 格式
# hsv = cv2.cvtColor(captcha_image_cv, cv2.COLOR_BGR2HSV)

# # 設定藍色範圍，過濾出藍色背景
# # 藍色的範圍可以根據實際情況調整
# lower_blue = np.array([90, 50, 50])
# upper_blue = np.array([130, 255, 255])
# mask = cv2.inRange(hsv, lower_blue, upper_blue)

# # 反轉遮罩，保留白色字元，將背景設為黑色
# mask_inv = cv2.bitwise_not(mask)
# result = cv2.bitwise_and(captcha_image_cv, captcha_image_cv, mask=mask_inv)

# # 將結果轉為灰度圖
# gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

# # 增強對比度
# enhancer = ImageEnhance.Contrast(Image.fromarray(gray))
# enhanced_image = enhancer.enhance(2)  # 增強對比度，數值可以調整

# # 轉換回 OpenCV 格式
# enhanced_image_cv = np.array(enhanced_image)

# # 使用 Otsu 的方法進行二值化
# _, binary = cv2.threshold(enhanced_image_cv, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# # 形態學操作：膨脹和腐蝕，以便更好地處理重疊文字
# kernel = np.ones((2, 2), np.uint8)
# binary = cv2.dilate(binary, kernel, iterations=1)  # 膨脹，加粗文字
# binary = cv2.erode(binary, kernel, iterations=1)   # 腐蝕，減少重疊

# # 使用 pytesseract 辨識驗證碼
# custom_config = r'--oem 3 --psm 8'  # 根據情況選擇合適的 psm 模式
# captcha_text = pytesseract.image_to_string(binary, config=custom_config)
# print(f"辨識出的驗證碼: {captcha_text}")

#checkbox = driver.find_element(By.ID, "TicketForm_agree").click()
if(driver.find_element(By.ID, "TicketForm_agree")):
    checkbox = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "TicketForm_agree"))  
    ).click()


verifyCode_fill = driver.find_element(By.ID, "TicketForm_verifyCode")
captcha_input = input('print')
# # verifyCode_fill.send_keys(captcha_text)
# verifyCode_fill.send_keys(captcha_input)

# if(driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary btn-green"]')):
#     confirm_button = WebDriverWait(driver, 5).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="btn btn-primary btn-green"]')) 
#     ).click()

# Select payment and delivery methods
if(driver.find_element(By.ID, "CheckoutForm_paymentId_54")):
    Transfer_money = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "CheckoutForm_paymentId_54"))   
    ).click()

if(driver.find_element(By.ID, "submitButton")):
    confirm_order_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "submitButton"))   
    ).click()

# 關閉瀏覽器
#driver.quit()

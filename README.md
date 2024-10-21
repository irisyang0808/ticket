<!-- # ticket

pip install selenium
pip install Pillow
pip install opencv-python


下拉式選單寫法範例
# choose day
select_day = driver.find_elements(By.TAG_NAME, value="Option")
i=0
while i < len(select_day):
    if(select_day[i].text == "2025/03/22 (六)"):
        select_day[i].click
    i=i+1 -->
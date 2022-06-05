from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#홍지수
driver=webdriver.Chrome()
driver.get("https://e-onestop.pusan.ac.kr/index?home=home")

driver.maximize_window()
name1=driver.find_elements_by_css_selector('#homeNotice > li > a')
for i in name1:
    b=i.text
    print(b)
#허경록
sleep(3)

driver.get("https://plato.pusan.ac.kr/")

id=input('아이디 입력> ')
pw=input('비밀번호 입력> ')

elem = driver.find_element_by_id("input-username")
elem.send_keys(f'{id}')
elem = driver.find_element_by_id("input-password")
elem.send_keys(f'{pw}')
elem.send_keys(Keys.RETURN)
sleep(2)

name2=driver.find_elements_by_css_selector('#page-content > div > div.front-box.front-box-notice > div.front-box-body > ul > li > a')
for j in name2:
    c=j.text
    print(c)
sleep(3)
driver.quit()





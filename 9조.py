from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://e-onestop.pusan.ac.kr/index?home=home")

driver.maximize_window()
name1=driver.find_elements_by_css_selector('#homeNotice > li > a')
for i in name1:
    b=i.text
    print(b)





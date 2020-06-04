from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

def sendAndSubmit(URL,username,pw,ISP):
    try:
        usernameInput=driver.find_elements_by_name("DDDDD")[1]
        usernameInput.clear()
        sleep(0.2)
        pwInput=driver.find_elements_by_name("upass")[1]
        pwInput.clear()
        sleep(0.3)
        ISPSelect=driver.find_element_by_name("ISP_select")
        #all_options = element.find_elements_by_tag_name("option")
        sleep(0.1)
        loginInput=driver.find_elements_by_name("0MKKey")[1]
        #loginInput.clear()
        sleep(0.25)
        usernameInput.send_keys(username)
        sleep(0.3)
        pwInput.send_keys(pw)
        sleep(0.15)
        Select(ISPSelect).select_by_visible_text(ISP)
        sleep(0.2)
        loginInput.submit()
        return 0
    except:
        return 1

URL="URL"
username="1907310000"
pw="000000"
ISP="选择ISP"
driver=webdriver.Chrome()
driver.get(URL)
sleep(0.2)
sumTimes=1

while sendAndSubmit(URL,username,pw,ISP) and sumTimes<=3 :
    print("ERROR!10s后进行第%d/3次重试"%(sumTimes))
    sleep(10)
    sumTimes=sumTimes+1
    
print("10秒后自动关闭窗口")
sleep(10)
driver.close()

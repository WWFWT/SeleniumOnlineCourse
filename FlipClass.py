#播放完成判断
#"vjs_mediaplayer"
#class中会有vjs-ended

#视频列表的item class="source-file-item"
#作业 id="homeworkColor_138595"
#视频 id="fileColor_1165268"
#播放速度 <div class="speedTab30" rate="3.0"></div>
#声音 <div class="volumeIcon"></div>
#标清 <b class="line1bq"></b>

import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driverPath="K:\SDK\chromedriver.exe"
url = 'https://passport.zhihuishu.com/login'
school = "学校名"
classNum = "学号"
passWord = "密码"
classTitle = "课程名称"
start = 45 #从第几课开始

browser = webdriver.Chrome(executable_path=driverPath)
browser.get(url)
wait = WebDriverWait(browser, 10)

def LogIn(school,username,password):
    try:
        browser.find_element_by_xpath("//a[@href='#studentID']").click()
        time.sleep(1)
        inputSchool = browser.find_element_by_xpath("//input[@placeholder='输入你的学校']")
        inputSchool.send_keys(school)
        time.sleep(1)
        inputSchool.send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element_by_xpath("//li[@value='1551']").click()
        browser.find_element_by_xpath("//input[@placeholder='大学学号']").send_keys(username)
        browser.find_element_by_xpath("//input[@placeholder='密码']").send_keys(password)
        browser.find_element_by_class_name('wall-sub-btn').click()
    except:
        print("登陆账号出错,请手动登陆,登陆完成后按回车继续")
        input()

def IsViewEnd():
    try:
        video = browser.find_element_by_id('vjs_mediaplayer')
        if 'vjs-ended' in video.get_attribute('class'):
            return True
        return False
    except:
        print("找不到播放结束标志")
        return False

if __name__ == "__main__":
    LogIn(school,classNum,passWord)
    print("登陆完成")

    time.sleep(5)
    print("进入我的学堂")
    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/ul/li[3]/a").click()

    time.sleep(5)
    print("获取所有课程")
    classList = browser.find_elements_by_xpath("//ul[@class='datalist']")

    print("进入指定课程")
    for i in classList:
        title = i.find_element_by_xpath("./div/dl/dt/div[1]")
        if title.text == classTitle:
            i.click()
            time.sleep(5)
            print("播放第一课,进入播放页面")
            browser.find_element_by_xpath("//div[@class='dt-name dt-takeup ']").click()
            time.sleep(5)

    n = browser.window_handles  # 获取当前页句柄
    browser.switch_to.window(n[1])  # 切换到新的网页窗口

    videoList=[]
    allList = browser.find_elements_by_xpath("//a[contains(@onclick,openStudySource)]")

    for i in allList:
        if i.get_attribute('onclick')!=None and ('.wmv' in i.text or '.mp4' in i.text):
            videoList.append(i.get_attribute('onclick'))

    for count,s in enumerate(videoList):
        if(count<start):
            count=count+1
            continue
        s='''//a[@onclick="'''+s+'''"]'''
        video = browser.find_element_by_xpath(s)
        print(f'当前视频: {count + 1:3d} / {len(videoList)}')

        try:
            video.click()
            time.sleep(3)
            videoArea = browser.find_element_by_class_name("videoArea")
            ActionChains(browser).move_to_element(videoArea).perform()

            # 设置静音volumeIcon
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'volumeIcon'))).click()

            # 设置3倍速
            speedBox = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "speedBox")))
            ActionChains(browser).move_to_element(speedBox).perform()
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'speedTab30'))).click()

            # 设置标清
            quality = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "definiBox")))
            ActionChains(browser).move_to_element(quality).perform()
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'line1bq'))).click()
            time.sleep(10)
        except:
            continue

        while 1:
            if(IsViewEnd()):
                print("播放完毕,切换下一个视频")
                break




#A选项 <svg aria-hidden="true" class="icon topic-option"><use xlink:href="#iconxuanzhong"></use></svg>
#关闭按钮 <span class="dialog-footer"><div class="btn">关闭</div></span>
#视频 <video id="vjs_container_html5_api" class="vjs-tech" poster="about:blank" autoplay="" src="https://wsvideo.zhihuishu.com/zhs/zhsmanage/video/201903/a55eac3c1c814a63aa8c96daa155f3dc_512.mp4"><p class="vjs-no-js">Sorry 您可能需要下载新版本的浏览器来支持html5并播放本视频. <br> 请下载如下浏览器: Firefox3.5+ 或 Chrome3+</p></video>
#播放按钮 <div id="playButton" class="playButton"><div class="bigPlayButton pointer" style="display: block;"></div></div>

#登陆
#<a href="#studentID" id="qStudentID">学号</a>
#<input class="school-search-ipt" placeholder="输入你的学校" type="text" id="quickSearch" autocomplete="off" onfocus="hideErrorInfo('form-ipt-error-c-school');" onclick="userindex.selectSchoolByName();" onkeyup="userindex.selectSchoolByName();">
#<input type="text" placeholder="大学学号" autocomplete="off" value="" onfocus="hideErrorInfo('form-ipt-error-cl-code');" maxlength="40" name="clCode" id="clCode">
#<input type="password" placeholder="密码" autocomplete="off" value="" name="clPassword" maxlength="40" onfocus="hideErrorInfo('form-ipt-error-cl-password');" id="clPassword">
#<li value="1551" slogo="https://image.zhihuishu.com/testzhs/zhsmanage/image/201609/9de5448d8b8e4e7f8a22aab82779631a.jpg"><b><font style="color:#3D84FF;">贺州学院</font></b></li>


#节点:id="vjs_container"
#节点 视频播放完毕 class="video-js vjs-default-skin able-player-skin vjs_container-dimensions vjs-controls-disabled vjs-workinghover vjs-has-started vjs-user-inactive vjs-paused vjs-ended"

import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

driverPath=r"K:\SDK\chromedriver.exe"
url = 'https://passport.zhihuishu.com/login'
school = "学校名"
classNum = "学号"
passWord = "密码"
classTitle = "课程名称"
start = 145 #从第几课开始

browser = webdriver.Chrome(executable_path=driverPath)
wait = WebDriverWait(browser, 10)
browser.get(url)

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

#检测是否播放完
def ViewIsEnd():
    try:
        # 读取当前进度
        video = browser.find_element_by_id("vjs_container")
        if "vjs-ended" in video.get_attribute("class"):
            print("播放完毕,切换下一个")
            return True
        return False
    except:
        return False

#关闭弹窗
def CloseTitle():
    try:
        #选个A并关闭
        browser.find_element_by_class_name('topic-item').click()
        time.sleep(1)
        browser.find_element_by_xpath("/html/body/div[1]/div/div[7]/div/div[1]/button").click()
        time.sleep(1)

        #继续播放
        ac = ActionChains(browser)
        e = browser.find_element_by_class_name('videoArea')
        ac.move_to_element_with_offset(e, 100, 100)
        ac.click()
        ac.perform()
    except:
        return



if __name__ == '__main__':
    try:
        browser.maximize_window()
        LogIn(school,classNum,passWord)

        time.sleep(5)
        print("进入在线学堂")
        browser.find_element_by_xpath("//a[@class='header-enter-school fl']").click()

        time.sleep(5)
        print("获取所有课程")
        classList = browser.find_elements_by_xpath("//ul[@class='datalist']")

        print("进入指定课程")
        for i in classList:
            title = i.find_element_by_xpath("./div/dl/dt/div[1]")
            if title.text == classTitle:
                i.click()
                time.sleep(5)
                break

        #关闭弹窗(有时不一定有)
        try:
            allClose = browser.find_elements_by_xpath("//div[@class='el-dialog__header']")
            for i in allClose:
                title = i.find_element_by_xpath("./span").text
                if title=="智慧树警告":
                    i.find_element_by_xpath("./button").click()
                    time.sleep(1)
                    break
            #关闭学前必读
            browser.find_element_by_xpath("//div[@class='dialog-read']/div/i").click()
        except:
            print("无弹窗")

        playlist = browser.find_elements_by_class_name('time_ico_half')
        for count, video in enumerate(playlist):
            if (count < start):
                continue
            try:
                video.click()
            except:
                continue

            time.sleep(5)  # 等待加载出来

            print(f'当前视频: {count + 1:3d} / {len(playlist)}')
            while 1:
                CloseTitle()
                time.sleep(3)
                if (ViewIsEnd()):
                    print("播放完毕,开始播放下一个")
                    break
    except EOFError:
        print('你中止了进程。')

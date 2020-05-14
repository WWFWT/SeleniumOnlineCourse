#登陆 <a class="f-f0 navLoginBtn" id="auto-id-1589429514492">登录<span class="huo">&nbsp;&nbsp;|&nbsp;&nbsp;</span>注册</a>
#手机登陆 <li class="last-login-holder z-sel"><!--Regular if239-->手机号登录</li>
#iframe <iframe name="" frameborder="0" id="x-URS-iframe1589432123516.209" scrolling="no" style="width: 100%; height: 100%; border: none; background: none;"
#账号 <input type="tel" maxlength="11" spellcheck="false" tabindex="1" autocomplete="off" class="dlemail j-nameforslide" name="email" placeholder="请输入手机号" id="phoneipt">
#密码 <input type="password" spellcheck="false" tabindex="2" autocomplete="new-password" class="j-inputtext dlemail" name="email" placeholder="请输入密码" id="auto-id-1589429565928">
#登陆 <a tabindex="8" id="submitBtn" class="u-loginbtn btncolor tabfocus ">登 录</a>

#我的课程 <div class="u-loginPerson-mycourse" data-cate="首页_个人面板框"><a href="//www.icourse163.org/home.htm?userId=1148031792" target="_top"><span>我的课程</span></a><div class="main-page-tip"><div class="arrow"></div><div class="text">现在制定学习计划，获取专属学习日历</div><a class="close-tip u-icon-normal-close"></a></div></div>

#选择课程
#继续学习 <a class="u-btn f-fr u-btn-orange u-btn-lg j-nextlink" href="#/learn/content?type=detail&amp;id=1214434745&amp;cid=1218129659" target="_self">继续学习</a>

#视频区域 class="mooc-video-player"
#2倍速 <li class="item z-sel" data-index="5">2倍速</li>
#静音 <div class="controlbar_btn volumebtn j-volumebtn" id="auto-id-1589428621374">


#输入框<textarea name="inputtxt" class="j-textarea inputtxt" id="auto-id-1589440170253" style="width: 240px; height: 25px;"></textarea>
#选项 <ul class="choices f-cb">
# <li class="f-cb  ">
# <input class="u-tbi" id="op_37806204959821589437117137" type="radio" name="op_12225354301589437117137">
# <label class="u-tbl f-pr f-cb" for="op_37806204959821589437117137">
# <div class="f-fl optionPos">A.</div>
# <div class="f-fl f-richEditorText optionCnt f-thide edueditor_styleclass_51">
# <span class="u-icon-correct"></span></div></label></li><li class="f-cb  ">
# <input class="u-tbi" id="op_137806204959821589437117137" type="radio" name="op_12225354301589437117137">
# <label class="u-tbl f-pr f-cb" for="op_137806204959821589437117137"><div class="f-fl optionPos">B.</div>
# <div class="f-fl f-richEditorText optionCnt f-thide edueditor_styleclass_52"><span class="u-icon-wrong"></span>
# </div></label></li></ul>
#提交<a class="u-btn u-btn-default submit j-submit" id="auto-id-1589437117740">提交</a>
#继续<a class="u-btn u-btn-default cont j-continue" id="auto-id-1589437117741" style="">继续学习</a>

from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

path = r"K:\SDK\chromedriver.exe"
url = "https://www.icourse163.org/"
number = "手机号"
passWord = "密码"


driver = webdriver.Chrome(executable_path=path)
driver.get(url)

def LogIn():
    driver.find_element_by_xpath("//a[@class='f-f0 navLoginBtn']").click()
    sleep(3)
    driver.find_element_by_xpath("//div[@class='ux-tabs-underline']/ul/li[2]").click()
    sleep(3)
    iframe = driver.find_element_by_xpath("//div[@id='j-ursContainer-1']/iframe")
    driver.switch_to.frame(iframe)
    driver.find_element_by_xpath("//input[@placeholder='请输入手机号']").send_keys(number)
    sleep(0.5)
    driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys(passWord)
    sleep(0.5)
    driver.find_element_by_id("submitBtn").click()
    sleep(1)
    if driver.find_element_by_xpath("div[@id='nerror']/div[2]").text == "请通过手机短信登录":
        driver.switch_to.default_content()
        return False
    driver.switch_to.default_content()
    return True

def ChooseClass(name):
    classList = driver.find_elements_by_class_name('course-card-wrapper')
    for i in classList:
        className = i.find_element_by_xpath("./div/a/div[2]/div[1]/div[1]/div/span[2]").text
        if className==name:
            i.find_element_by_xpath("./div/a").click()
            sleep(5)
            return True
    return False

def CloseTitle():
    try:
        try:
            driver.find_element_by_xpath("//ul[@class='choices f-cb']/li[1]/input").click()
            sleep(1)
            driver.find_element_by_xpath("//textarea[@name='inputtxt']").send_keys("123456")
            sleep(1)
        except:
            pass
        driver.find_element_by_xpath("//a[@class='u-btn u-btn-default submit j-submit']").click()
        sleep(1)
        driver.find_element_by_xpath("//a[@class='u-btn u-btn-default cont j-continue']").click()
    except:
        pass

if __name__ == "__main__" :
    try:
        print("自动登陆")
        if(False==LogIn()):
            input("自动登陆失败,请手动登陆后(或者已经登陆)按回车继续...")
        sleep(5)
    except:
        input("自动登陆失败,请手动登陆后(或者已经登陆)按回车继续...")
    print("进入我的课程")
    driver.find_element_by_xpath("//div[@data-cate='首页_个人面板框']/a").click()
    sleep(5)
    n = driver.window_handles  # 获取当前页句柄
    driver.switch_to.window(n[1])  # 切换到新的网页窗口

    if ChooseClass("MySQL数据库设计与应用")==False:
        input("找不到课程")
        exit(1)

    print("继续学习")
    n = driver.window_handles  # 获取当前页句柄
    driver.switch_to.window(n[2])  # 切换到新的网页窗口
    driver.find_element_by_xpath("//a[@class='u-btn f-fr u-btn-orange u-btn-lg j-nextlink']").click()
    while 1:
        sleep(5)
        try:
            driver.find_element_by_xpath("//div[@class='controlbar_btn volumebtn j-volumebtn']").click()
            video = driver.find_element_by_xpath("//div[@class='ux-video-player']")
            ActionChains(driver).move_to_element(video)
            sleep(1)
            pos = driver.find_element_by_xpath("//div[@class='controlbar_btn ratebtn j-ratebtn']/div")
            ActionChains(driver).move_to_element(pos)
            driver.find_element_by_xpath("//div[@class='m-popover m-popover-rate']/ul/li[5]").click()
        except:
            pass
        CloseTitle()


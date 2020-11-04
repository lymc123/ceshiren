from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestSigln:
    def setup_class(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['deviceName'] = '1e074177'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.LaunchSplashActivity'
        #
        caps['noReset'] ='true'
        caps['dontStopAppOnReset']='true'
        caps['skipDeviceInitialization']='true'
        caps['skipServerInstallation']='true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)

    def test_workspace(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        print("进入工作台")
        sleep(2)

    def test_sigin(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .textContains("打卡").instance(0));').click()
        print("滑屏到打卡")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        print("进入打卡页面")
        self.driver.update_settings({"waitForIdleTimeout": 0})
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        print("开始打卡")

        element = WebDriverWait(self.driver,10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']"))
        element.click()

    def teardown_class(self):
        self.driver.quit()
